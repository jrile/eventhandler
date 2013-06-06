""" 
TODO: fix date default
spread drive search/browse results across pages.
search folders/files as well?
"""

import sys,  CSSystem
from PyQt4 import QtCore,  QtGui
import AdminTools,  CSDialogs,  Database
from login_ui import *
from main_ui import *

#global mysql connection
db = Database.Database() 
ADMIN_LEVEL = 3
class Login(QtGui.QMainWindow):
    """Main login class that will show up first.
    Checks database to ensure that it's an authorized user.
    If no username/password combo is found, error message is shown, 
    else, main window is brought up."""
    
    def __init__(self,parent=None):
        """Brings the login screen into focus."""
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.usernameValue.setFocus()
        self.ui.loginButton.setAutoDefault(True)
        self.ui.cancelButton.setAutoDefault(True)

    def accept(self):
        """User has clicked okay or pressed return, verify login is valid."""
        self.username = str(self.ui.usernameValue.text())
        password = str(self.ui.passwordValue.text())
        result = db.login(self.username,  password)
        if result is None:
            self.login_error()
        else:
            # success! bring up main window.
            self.level = result[0]
            self.hide()
            mainwindow = Main(self)
            if self.level == ADMIN_LEVEL:
                mainwindow.ui.addAdminTools(mainwindow)
            mainwindow.show()

    def login_error(self):
        self.ui.usernameValue.setText("")
        self.ui.passwordValue.setText("")
        self.ui.usernameValue.setFocus()
        QtGui.QMessageBox.warning(self, "Error!", "Invalid login, please try again.")

    def reject(self):
        # if the login is cancelled, close the program.
        sys.exit()
        
class Main(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        """The main window. Shows hard drive query results, also has a file menu."""
        self.username = parent.username
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.search_dialog = CSDialogs.Search(self)
        self.drive_selected_dialog = CSDialogs.FolderView(self)
        self.add_user_dialog = AdminTools.AddUser(self)
        self.del_user_dialog = AdminTools.DelUser(self)
        self.edit_user_dialog = AdminTools.EditUser(self)
        self.addAndBackupDialogs()
    
    def addAndBackupDialogs(self):
        """Bring up dialogs concerning hard drive information."""
        try:
            self.add_hard_drive_dialog = CSDialogs.SelectHDD(self)
            self.backup_hard_drive_dialog = CSDialogs.BackupHDD(self)
        except CSSystem.SystemException as e:
            print e
            self.root = False
        else:
            self.root = True
    
    def refresh(self):
        try:
            self.add_hard_drive_dialog.close()
            self.backup_hard_drive_dialog.close()
        except AttributeError:
            # can't access hard drive information
            self.hardDriveError()
        else:              
            self.addAndBackupDialogs()

    def hardDriveError(self):
        QtGui.QMessageBox.warning(self, "Error!", "Error getting information from hard drive. Please try again as root user.")            

    def addUser(self):
        self.add_user_dialog.show()
        
    def delUser(self):
        self.del_user_dialog.show()
        
    def editUser(self):
        self.edit_user_dialog.show()

    def about(self):
        QtGui.QMessageBox.information(self, "About", "Copy Station\nVersion 1.0.1\n(c) 2013 Eastcor Engineering")
        
    def add_hard_drive(self):
        """Brings up add hard drive dialog. Adds hard drive to database."""
        if self.root:
            self.add_hard_drive_dialog.show()
        else:
            self.hardDriveError()
        
    def browse(self):
        """Displays all drives in database."""
        self.display_drives(db.browse())

    def make_backup(self):
        if self.root:
            pt = ProgressThread(self)
            pt.start()
            self.backup_hard_drive_dialog.show()
        else:
            self.hardDriveError()           
           
        
    def search(self):
        """Opens dialog to search for hard drives."""
        self.search_dialog.show()
        if self.search_dialog.exec_():
            query = self.search_dialog.getResults()
            if query:
                results = db.search(query)
                if not results:
                    QtGui.QMessageBox.warning(self,  "Error!", "No items found.")
                    self.ui.tableWidget.setRowCount(0)
                else:
                    self.display_drives(results)
            else:
                QtGui.QMessageBox.warning(self, "Error!", "Select at least one item to search for!")
                
    def display_drives(self,  values):
        """Puts drive information from database into main window."""
        self.ui.tableWidget.setSortingEnabled(False)
        self.ui.tableWidget.setRowCount(0) # clear table before new search/browse
        for i in range(0,  len(values)):
            self.ui.tableWidget.insertRow(i)
            self.ui.tableWidget.setItem(i,  0,  QtGui.QTableWidgetItem(values[i][0]))
            self.ui.tableWidget.setItem(i,  1,  QtGui.QTableWidgetItem(values[i][1]))
            self.ui.tableWidget.setItem(i,  2,  QtGui.QTableWidgetItem(unicode(values[i][2])))
            self.ui.tableWidget.setItem(i,  3,  QtGui.QTableWidgetItem(values[i][3]))
            self.ui.tableWidget.setItem(i,  4,  QtGui.QTableWidgetItem(str(values[i][4])))
        self.ui.tableWidget.setSortingEnabled(True)

    def drive_selected(self,  x,  _):
        """Opens up the drive/folder view for the drive.."""
        ser = self.ui.tableWidget.item(x,  0).text()
        d_n = self.ui.tableWidget.item(x,  1).text()
        self.drive_selected_dialog.set(ser,  d_n)
        if self.drive_selected_dialog.getResults():
            self.drive_selected_dialog.displayResults()
            self.drive_selected_dialog.show()
        else:
            QtGui.QMessageBox.warning(self,  "Error!", "No folders found for this drive.")
            
class ProgressThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(ProgressThread, self).__init__()
        self.progress = QtGui.QProgressDialog("Backing up", "Cancel", 0, 100000, parent)
        self.progress.show()
        QtCore.QObject.connect(self.progress, QtCore.SIGNAL("cancelled()"), parent.backup_hard_drive_dialog.cancelled)

##############################################################
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp=Login()
    myapp.show()
    sys.exit(app.exec_())
