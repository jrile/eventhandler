# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/edit_user.ui'
#
# Created: Mon Jun 10 08:20:12 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditUser(object):
    def setupUi(self, EditUser):
        EditUser.setObjectName("EditUser")
        EditUser.resize(320, 240)
        self.verticalLayout = QtGui.QVBoxLayout(EditUser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(EditUser)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username = QtGui.QLineEdit(EditUser)
        self.username.setMaxLength(20)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(EditUser)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.password = QtGui.QLineEdit(EditUser)
        self.password.setStyleSheet("QLineEdit{background:#CCCCCC;}")
        self.password.setMaxLength(20)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setReadOnly(True)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(EditUser)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.name = QtGui.QLineEdit(EditUser)
        self.name.setStyleSheet("QLineEdit{background:#CCCCCC;}")
        self.name.setMaxLength(40)
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(EditUser)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.level = QtGui.QLineEdit(EditUser)
        self.level.setMaximumSize(QtCore.QSize(35, 16777215))
        self.level.setStyleSheet("QLineEdit{background:#CCCCCC;}")
        self.level.setMaxLength(1)
        self.level.setReadOnly(True)
        self.level.setObjectName("level")
        self.gridLayout.addWidget(self.level, 4, 1, 1, 1)
        self.check = QtGui.QPushButton(EditUser)
        self.check.setMaximumSize(QtCore.QSize(120, 16777215))
        self.check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check.setObjectName("check")
        self.gridLayout.addWidget(self.check, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(EditUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditUser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EditUser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EditUser.reject)
        QtCore.QObject.connect(self.check, QtCore.SIGNAL("clicked()"), EditUser.check)
        QtCore.QMetaObject.connectSlotsByName(EditUser)

    def retranslateUi(self, EditUser):
        EditUser.setWindowTitle(QtGui.QApplication.translate("EditUser", "Edit User", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditUser", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditUser", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditUser", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditUser", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.check.setText(QtGui.QApplication.translate("EditUser", "Check", None, QtGui.QApplication.UnicodeUTF8))

