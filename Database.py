"""
Functions that connect to the database and get information.
TODO: 
- sha1 not 100% secure.

"""

import os, os.path, mysql.connector
# global mysql connection/cursor
connection = mysql.connector.connect(user='root',
                                         database='test')
cursor = connection.cursor()


class DatabaseException(Exception):
    pass

class Database():
    
    def search(self,  query):
        cursor.execute(query)
        return cursor.fetchall()
        
    def getCopies(self, serial):
        cursor.execute("select count(*) from master_drive where is_backup_of = \'%s\'" % serial)
        return cursor.fetchone()[0]
        
    def browse(self):
        cursor.execute("select *, (select count(*) from master_drive where is_backup_of = a.serial) from master_drive a")
        return cursor.fetchall()
        
    def addOrUpdateLocation(self, serial, location):
        if not location: # if left blank when updated, delete location information
            cursor.execute("delete from location where serial = \'%s\'" % serial)
        else:
            query = "insert into location (serial, location) values (%s, %s) on duplicate key update location=%s"
            cursor.execute(query,  (serial, location, location))
        
    def getLocation(self, serial):
        query = "select location from location where serial = \'%s\'" % serial
        cursor.execute(query)
        return cursor.fetchall()
        
    def addUser(self,  username, passhash, level,  name=None):
        if not name:
            query = "insert into users (username, passhash, level) values (%s, sha1(%s), %s)"
            cursor.execute(query,  (username, passhash,  level))
        else:
            query = "insert into users (username, passhash, name, level) values (%s, sha1(%s), %s, %s)"
            cursor.execute(query,  (username,  passhash,  name,  level))
            
    def delUser(self,  username):
        if self.exists(username):
            query = "delete from users where username = \'%s\'" % username
            cursor.execute(query)
        else:
            raise DatabaseException("User does not exist.")
            
    def editUser(self,  name, level,  username,  password=None):
        if password:
            query = "update users set name = %s, passhash = sha1(%s), level = %s where username = %s"
            cursor.execute(query,  (name,  password,  level,  username))
        else:
            query = "update users set name = %s,level = %s where username = %s"
            cursor.execute(query,  (name, level,  username))           

    def login(self,  username,  password):
        query = ("select level from users where "
                    "username = %s and passhash = sha1(%s)")
        # check if username/password combo exists on database
        # return user level 
        cursor.execute(query, (username, password))
        return cursor.fetchone()
        
    def exists(self,  username):
        query = ("select count(*) from users where "
                 "username = \'%s\'") % username
        cursor.execute(query)
        return cursor.fetchone()[0]

    def checkIfDriveExists(self, serial, name):
        query = ("select 1 from master_drive where "
                 "serial = %s and drive_name = %s")
        cursor.execute(query, (serial, name))
        if cursor.fetchone() is None:
            return False
        return True

    def addHardDrive(self, serial,  username,  mount, backup_serial=None, backup_name=None):
        """Adds a hard drive to the 'master_drive' table.
        Check to see if exists in database, if not add everything to database."""
        if not backup_serial:
            query = ("insert ignore into master_drive (serial, drive_name, "
                    "username) values (%s, %s, %s)")
            cursor.execute(query, (serial, mount, username))
        else:
            self.addHardDrive(backup_serial, username, backup_name) # if the original hard drive hasn't been added, add it.
            query = ("insert ignore into master_drive (serial, drive_name, "
                            "username, is_backup_of) values (%s,  %s, %s, %s)"  )
            cursor.execute(query, (serial, mount, username, backup_serial))
        self.add(mount, serial)

    def add(self, path, serial):
        """Given a directory, iterates through to find subdirectories.
        Adds all subdirectories to `data_folder` table, and sends folder path
        on to addFiles."""

        add_path = ("insert IGNORE into data_folders "
                    "(serial, folder_name) "
                    "values (%s, %s)")
        for f in os.listdir(path):
            if os.path.isdir(path+"//"+f):
                cursor.execute(add_path,  (serial,  f))
                get_seq = ("select folder_sequence from data_folders "
                                "where folder_name = %s and serial = %s")
                cursor.execute(get_seq,  (f,  serial))
                sequence = cursor.fetchone()[0]
                self.addFiles(os.path.join(path,  f),  sequence)        


    def addFiles(self, path, sequence):     
        add_file = ("insert IGNORE into data_files "
                    "(folder_sequence, file_name) "
                    "values (%s, %s)")
        for filename in os.listdir(path):
            data = (sequence, filename)
            cursor.execute(add_file, data)
