# Copy Station Dialogs
# Contains all of the regular-user dialogs that appear on the Copy Station GUI.

import shutil,  os, datetime, mysql.connector.errors
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
    Displays drive contents, allows user to edit location."""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
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
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        self.ui.drive_name.setFocus()
        date = datetime.date.today()
        year = date.year
        month = date.month
        day = date.month
        qd = QtCore.QDate(year, month, day)
        before_qd = qd.addMonths(-1)
        # set before date to one month prior to today, after date to today
        self.ui.before.setDate(before_qd)
        self.ui.after.setDate(qd)
     
    def getResults(self):
        """Given input, searchs database for a hard drive/filename match."""
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
        query = "select distinct master_drive.serial, drive_name, date_added, username, is_backup_of from master_drive "
        if filename:
            query += "inner join data_folders inner join data_files "
        query += "where "
        if filename:
            query += "file_name = \'%s\' AND " % filename
        if serial:
            query += "serial like \'%s\' AND " % serial
        if drive_name:
            query += "drive_name like \'%s\' AND " %drive_name
        if date_check:
            query += "date_added between str_to_date(\'%s\', \'%%m/%%d/%%Y\') and str_to_date(\'%s\', \'%%m/%%d/%%Y\') AND " % (before_date, after_date)
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
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Location()
        self.ui.setupUi(self)
        
    def set(self, serial, drive_name):
        self.serial = serial
        self.drive_name = drive_name
        location = db.getLocation(self.serial)
        if not location:
            location_text = "There is no location information on file."
        else:
            location_text = "Location:\n" + location[0]
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
        QtGui.QDialog.__init__(self,parent)
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
                name = system.getName(system.getMountPoint(path))
                mount = system.getMountPoint(path)
                db.addHardDrive(serial,  self.username,  name, mount)


class BackupHDD(QtGui.QDialog):
    def __init__(self,parent=None):
        """Dialog box to back up a hard drive and add both hard drives to database."""
        self.size = 0
        QtGui.QDialog.__init__(self,parent)
        self.parent = parent
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
        for i in range(len(self.mounted_hdds)-1):
            comboBox = QtGui.QComboBox()
            comboBox.addItems(self.mounted_hdds)
            comboBox.addItem("---")
            comboBox2 = QtGui.QComboBox()
            self.mounted_hdds.reverse()
            comboBox2.addItems(self.mounted_hdds)
            comboBox2.addItem("---")
            self.ui.backupTable.insertRow(i)
            #self.ui.backupTable.setItem(i,  0, QtGui.QTableWidgetItem(self.mounted_hdds[i]))
            self.ui.backupTable.setCellWidget(i, 0, comboBox)
            self.ui.backupTable.setCellWidget(i,  1, comboBox2)
                    
    def accept(self):
        super(BackupHDD, self).accept()
        try:
            self.processBackup()
        except mysql.connector.errors.IntegrityError:
            QtGui.QMessageBox.warning(self,  "Error!", "Serial for destination hard drive already exists in system! Please try another hard drive.")            
            
    def show(self):
        super(BackupHDD, self).show()
        if len(self.mounted_hdds) < 2:
            QtGui.QMessageBox.warning(self, "Error!", "Need more than one mounted hard drive to back up!")
        
    def processBackup(self):
        for row in range(0, self.ui.backupTable.rowCount()):
           source = str(self.ui.backupTable.cellWidget(row, 0).currentText())
           dest = str(self.ui.backupTable.cellWidget(row, 1).currentText())
           if source == dest:
                QtGui.QMessageBox.warning(self,  "Error!", "Can't copy " + source + " to itself!")
                continue
           if dest != '---' and source != '---':
               self.copy(source, dest)             
               
    def copy(self, source, target):
        source_mount_point = system.getMountPoint(source)
        source_name = system.getName(source_mount_point)
        dest_mount_point = system.getMountPoint(target)
        dest_name = system.getName(dest_mount_point)
        self.total_size = system.getDirSize(source_mount_point)
        #monkey patch shutil so we can get a progress report of what's going on
        shutil.copy2_old = shutil.copy2 
        def copy2(src, dst): 
            print "Copying: " + src
            shutil.copy2_old(src, dst) 
            self.size += os.path.getsize(src)
            print self.size, "/",   self.total_size, "bytes\t\t",  '%.1f' % ((float(self.size)/float(self.total_size))*100) + "%\n"
        shutil.copy2 = copy2 
        for item in os.listdir(source_mount_point):
            s = os.path.join(source_mount_point, item)
            d = os.path.join(dest_mount_point, item)
            if os.path.isdir(s):
                try:
                    shutil.copytree(s, d)
                except OSError, e:
                    if e.errno != 17: # 17 = folder already exists (comes up with Trash folder often)
                        raise              # ignore if 17, else raise it.
                    print "Copying: " + e.filename + " - path already exists on destination hard drive!!"
                    self.size += system.getDirSize(d)
                    print self.size, "/",   self.total_size, "bytes\t\t",  '%.1f' % ((float(self.size)/float(self.total_size))*100) + "%\n"
                    pass
            else:
                shutil.copy2(s, d) 
        print "Adding to database..."
        db.addHardDrive(system.getSerial(target), self.username,  dest_name, dest_mount_point, system.getSerial(source), source_name, source_mount_point)
        print "Done!"              
