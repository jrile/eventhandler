# Copy Station Dialogs
# Contains all of the regular-user dialogs that appear on the CS GUI.

import sys, shutil,  os,  mysql.connector,  threading
from PyQt4 import QtCore, QtGui
from Database import *
from CSSystem import *
from search_ui import *
from select_ui import *
from folder_view_ui import *
from backup_ui import *
from location_ui import *
from copying_ui import *

db = Database()
system = CSSystem()


class FolderView(QtGui.QDialog):
    """The view that appears when a user clicks on a hard drive from the main window.
    Displays drive contents, allows user to make a copy and allows user to view pre-existing copies."""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_FolderView()
        self.ui.setupUi(self)
        self.location_dialog = Location(self)

        
    def set(self,  serial, drive_name):
        self.ui.folder.clear()
        self.serial = serial
        self.drive_name = drive_name
        self.num_copies = db.getCopies(str(serial))
        self.ui.copyLabel.setText(QtGui.QApplication.translate("FolderView", "# copies: " + str(self.num_copies), None, QtGui.QApplication.UnicodeUTF8))


    def getResults(self):
        """Retrieves all `data_folders` associated with the hard drive's serial number.
        If no results are found, there are no folders under this drive."""
        query = "select * from data_folders where serial = \'%s\'" % self.serial
        self.folders = db.search(query)
        if not self.folders:
            return False
        return True
        
    def displayResults(self):
        """Display each folder in the GUI. Pass the folder item to `addFiles`."""
        for folder in self.folders:
            sequence = folder[0]
            parent = QtGui.QTreeWidgetItem(QtCore.QStringList(str(folder[2])))
            self.ui.folder.addTopLevelItem(parent)
            self.addFiles(parent,  sequence)

    def addFiles(self,  parent,  sequence):
        """Display each file under the appropriate folder in the GUI."""
        query = "select * from data_files where folder_sequence = %s" % sequence
        files = db.search(query)
        for file in files:
            temp = QtGui.QTreeWidgetItem(QtCore.QStringList(str(file[2])))
            parent.addChild(temp)
        
    def location(self):
        self.location_dialog.set(self.serial, self.drive_name)
        self.location_dialog.show()
        
class Search(QtGui.QDialog):
    """Search dialog box."""
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        self.ui.drive_name.setFocus()
     
    def getResults(self):
        """Given input, searchs database for a hard drive match."""
        serial = str(self.ui.serial.text())
        drive_name = str(self.ui.drive_name.text())
        date_check = self.ui.date_check.checkState()
        before_date = str(self.ui.before.text())
        after_date = str(self.ui.after.text())
        username = str(self.ui.username.text())
        filename = str(self.ui.filename.text())

        if not serial and not drive_name and not date_check and not username and not filename:
            # user has not inputted anything. Main window will display an error message.
            return None
        query = "select serial, drive_name, date_added, username, is_backup_of from master_drive "
        if filename:
            query += "inner join data_folders inner join data_files "
        query += "where "
        if filename:
            query += "file_name like \'%s\' AND " % filename
        if serial:
            query += "serial like \'%s\' AND " % serial
        if drive_name:
            query += "drive_name like \'%s\' AND " %drive_name
        if date_check:
            query += "date_added between \'%s\' and \'%s\' AND " % (after_date,  before_date)
        if username:
            query += "username like \'%s\'" % username
        elif (serial or drive_name or date_check or filename):
            # get rid of unnecessary "AND"
            query = query[:-5]
        # we have some information to search with.
        # send query to get search results and display in main window if query is sucessful.
        return query
            

class Location(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Location()
        self.ui.setupUi(self)
        
    def set(self, serial, drive_name):
        self.serial = serial
        self.drive_name = drive_name
        location = db.getLocation(self.serial)
        if not location:
            location_text = "There is no location information on file."
        else:
            location_text = "Location:\n"
            for i in location:
                for j in i:
                    location_text += str(j)
        self.ui.label.setText(QtGui.QApplication.translate("Location", "Location for...\n" + serial + "\n" +drive_name +":\n\n" + location_text,  
                                                           None, QtGui.QApplication.UnicodeUTF8))
                                                           
    def accept(self):
       db.addOrUpdateLocation(str(self.serial),  str(self.ui.locationBox.toPlainText()))
       QtGui.QMessageBox.information(self, "Confirmation", "Location updated successfully.")
       self.ui.locationBox.setPlainText("")
       super(Location, self).accept()


class SelectHDD(QtGui.QDialog):
    def __init__(self,parent=None):
        """Dialog box to add new hard drives to database."""
        QtGui.QWidget.__init__(self,parent)
        self.username = parent.username
        self.ui = Ui_SelectHDD()
        self.ui.setupUi(self)
        self.hdds = system.findHardDrives()
        for hdd in self.hdds:
            serial = system.getSerial(hdd)
            name = system.getMountPoint(hdd)
            if not serial or not name: continue # can't access information needed, skip this drive.
            self.ui.hddList.addItem(QtGui.QApplication.translate("SelectHDD",  hdd+
                                                                           "\n"+serial+"\n"+name,  None,  
                                                                           QtGui.QApplication.UnicodeUTF8))
       
    def accept(self):
        super(SelectHDD,  self).accept()
        for i in range(0,  self.ui.hddList.count()):
            if self.ui.hddList.item(i).isSelected():
                # this hard drive is to be added to the database.
                drive_info = str(self.ui.hddList.item(i).text()).split()
                path = drive_info[0]
                serial = drive_info[1]
                name = system.getMountPoint(path)
                db.addHardDrive(serial,  self.username,  name)


class BackupHDD(QtGui.QDialog):
    def __init__(self,parent=None):
        """Dialog box to add new hard drives to database."""
        QtGui.QWidget.__init__(self,parent)
        self.username = parent.username
        self.ui = Ui_BackupHDD()
        self.ui.setupUi(self)
        hdds = system.findHardDrives()
        self.mounted_hdds = []
        for hdd in hdds:
            serial = system.getSerial(hdd)
            name = system.getMountPoint(hdd)
            if serial and name:
                self.mounted_hdds.append(hdd)    
        self.ui.backupTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        for i in range(len(self.mounted_hdds)):
            self.ui.comboBox = QtGui.QComboBox(self)
            self.ui.comboBox.addItem("Don't backup")
            self.ui.comboBox.addItems(self.mounted_hdds)
            self.ui.backupTable.insertRow(i)
            self.ui.backupTable.setItem(i,  0, QtGui.QTableWidgetItem(self.mounted_hdds[i]))
            self.ui.backupTable.setCellWidget(i,  1, self.ui.comboBox)
                    
    def accept(self):
        super(BackupHDD, self).accept()
        try:
            self.processBackup()
        except mysql.connector.errors.IntegrityError:
            QtGui.QMessageBox.warning(self,  "Error!", "Backup already exists in system!")            
        
    def processBackup(self):
        for row in range(0, self.ui.backupTable.rowCount()):
           source = str(self.ui.backupTable.item(row, 0).text())
           dest = str(self.ui.backupTable.cellWidget(row, 1).currentText())
           if source == dest:
                QtGui.QMessageBox.warning(self,  "Error!", "Can't copy " + source + " to itself!")
                continue
           if dest != 'Don\'t backup':
               self.hide()
               self.backupCopy = BackupCopy(source, dest, self.username)
               self.backupCopy.run()

class BackupCopy(QtCore.QThread):
    # note, this will not work if folder already exists!!
    def __init__(self, source, dest, username):
        self.size = 0
        source_mount_point = system.getMountPoint(source)
        dest_mount_point = system.getMountPoint(dest)
        self.total_size = system.getDirSize(source_mount_point)
        QtCore.QThread.__init__(self)
        self.copy(source_mount_point, dest_mount_point)
        db.addHardDrive(system.getSerial(dest), username,  dest_mount_point, system.getSerial(source), source_mount_point)
        
    def copy(self, source, target):
        #monkey patch shutil so we can get a progress report of what's going on
        shutil.copy2_old = shutil.copy2 
        def copy2(src, dst): 
            print "Copying: " + dst
            shutil.copy2_old(src, dst) 
            self.size += os.path.getsize(src)
            print self.size, "/",   self.total_size, "bytes\t\t",  '%.1f' % ((float(self.size)/float(self.total_size))*100) + "%\n"
        shutil.copy2 = copy2 
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(target, item)
            if os.path.isdir(s):
                try:
                    shutil.copytree(s, d)
                except OSError, e:
                    if e.errno != 17: # 17 = file already exists (comes up with Trash folder often)
                        raise              # ignore if 17, else raise it.
                    print "Copying: " + e.filename + " - path already exists on destination hard drive!!"
                    self.size += system.getDirSize(d)
                    print self.size, "/",   self.total_size, "bytes\t\t",  '%.1f' % ((float(self.size)/float(self.total_size))*100) + "%\n"
                    pass
            else:
                shutil.copy2(s, d)   
        print "Done!"

     
