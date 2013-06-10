"""
Copy Station Administrator Tools
Special menu for users with administrator rights. Gives them access to user functionality.
TODO:
sha1 not secure
"""
from PyQt4 import QtCore, QtGui
from add_user_ui import *
from delete_user_ui import *
from edit_user_ui import *
import Database


class AddUser(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_AddUser()
        self.ui.setupUi(self)
        self.ui.username.setFocus()
        
    def accept(self):
        if not self.ui.username.text() or not self.ui.password.text():
            QtGui.QMessageBox.warning(self, "Error!", "Please fill all required fields.")
        else:
           try:
               lvl = int(self.ui.level.text())
               Database.Database().addUser(str(self.ui.username.text()), str(self.ui.password.text()),  
                                                                lvl,  str(self.ui.name.text()))
           except ValueError:
                QtGui.QMessageBox.warning(self,  "Error",  "Level is not a valid input.")
           except: 
                QtGui.QMessageBox.warning(self, "Error!", "Username already exists!")
                self.ui.username.setFocus()
           else:
                QtGui.QMessageBox.information(self, "Confirmation", "User successfully added.")
                self.ui.username.setText("")
                self.ui.password.setText("")
                self.ui.name.setText("")
                self.ui.level.setText("1")
                super(AddUser,  self).accept()


class DelUser(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DelUser()
        self.ui.setupUi(self)
        self.ui.username.setFocus()
        
    def accept(self):
        if not self.ui.username.text():
            QtGui.QMessageBox.warning(self, "Error!", "Please fill all required fields.")
        else:
            try:
                Database.Database().delUser(str(self.ui.username.text()))
            except(Database.DatabaseException):
                QtGui.QMessageBox.warning(self, "Error!", "User does not exist.")
                self.ui.username.setFocus()
            else:
                QtGui.QMessageBox.information(self,  "Confirmation",  "User successfully deleted.")
                self.ui.username.setText("")
                super(DelUser,  self).accept()
                
class EditUser(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EditUser()
        self.ui.setupUi(self)
        self.ui.username.setFocus()
        self.ui.check.setDefault(True)
    
    def check(self):
        if Database.Database().exists(self.ui.username.text()):
            self.ui.username.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            self.ui.username.setReadOnly(True)
            self.ui.password.setReadOnly(False)
            self.ui.name.setReadOnly(False)
            self.ui.level.setReadOnly(False)
            self.ui.password.setStyleSheet("")
            self.ui.name.setStyleSheet("")
            self.ui.level.setStyleSheet("")
            query = "select name, level from users where username = \'%s\'" % self.ui.username.text()
            results = Database.Database().search(query)[0]
            if results[0]:
                self.ui.name.setText(results[0])
            self.ui.level.setText(str(results[1]))
            self.ui.password.setFocus()
        else:
            QtGui.QMessageBox.warning(self,  "Error",  "Username not found.")
            self.ui.username.setFocus()
        
    def accept(self):
        try:
            lvl = int(self.ui.level.text())
        except(ValueError):
            QtGui.QMessageBox.warning(self,  "Error",  "Invalid input!")
        else:
            Database.Database().editUser(str(self.ui.name.text()),  str(self.ui.level.text()),  
                                                    str(self.ui.username.text()), str(self.ui.password.text()))     
            QtGui.QMessageBox.information(self,  "Confirmation",  "User successfully updated.")
            self.ui.username.setStyleSheet("")
            self.ui.username.setReadOnly(False)
            self.ui.password.setReadOnly(True)
            self.ui.name.setReadOnly(True)
            self.ui.level.setReadOnly(True)
            self.ui.name.setText("")
            self.ui.level.setText("")
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.name.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            self.ui.password.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            self.ui.level.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            super(EditUser,  self).accept()
    def reject(self):
            self.ui.username.setStyleSheet("")
            self.ui.username.setReadOnly(False)
            self.ui.password.setReadOnly(True)
            self.ui.name.setReadOnly(True)
            self.ui.level.setReadOnly(True)
            self.ui.name.setText("")
            self.ui.level.setText("")
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.name.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            self.ui.password.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            self.ui.level.setStyleSheet("QLineEdit{background:#CCCCCC;}")
            super(EditUser,  self).reject()
