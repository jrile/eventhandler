# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/edit_user.ui'
#
# Created: Tue Jun  4 15:32:51 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(320, 240)
        self.verticalLayout = QtGui.QVBoxLayout(AddUser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(AddUser)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username = QtGui.QLineEdit(AddUser)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AddUser)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtGui.QLineEdit(AddUser)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(AddUser)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.name = QtGui.QLineEdit(AddUser)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(AddUser)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.level = QtGui.QLineEdit(AddUser)
        self.level.setMaximumSize(QtCore.QSize(35, 16777215))
        self.level.setMaxLength(1)
        self.level.setObjectName("level")
        self.gridLayout.addWidget(self.level, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddUser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddUser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddUser.reject)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        AddUser.setWindowTitle(QtGui.QApplication.translate("AddUser", "Edit User", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddUser", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddUser", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddUser", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddUser", "Level:", None, QtGui.QApplication.UnicodeUTF8))

