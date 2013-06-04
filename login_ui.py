# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created: Tue Jun  4 15:42:49 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(433, 172)
        Login.setMinimumSize(QtCore.QSize(433, 172))
        self.verticalLayoutWidget = QtGui.QWidget(Login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 141, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.usernameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout.addWidget(self.usernameLabel)
        self.usernameValue = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.usernameValue.setMinimumSize(QtCore.QSize(0, 21))
        self.usernameValue.setMaximumSize(QtCore.QSize(139, 16777215))
        self.usernameValue.setObjectName("usernameValue")
        self.verticalLayout.addWidget(self.usernameValue)
        self.passwordLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout.addWidget(self.passwordLabel)
        self.passwordValue = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.passwordValue.setMinimumSize(QtCore.QSize(0, 21))
        self.passwordValue.setMaximumSize(QtCore.QSize(139, 16777215))
        self.passwordValue.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordValue.setObjectName("passwordValue")
        self.verticalLayout.addWidget(self.passwordValue)
        self.horizontalLayoutWidget = QtGui.QWidget(Login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 40, 162, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.retranslateUi(Login)
        QtCore.QObject.connect(self.passwordValue, QtCore.SIGNAL("returnPressed()"), Login.accept)
        QtCore.QObject.connect(self.loginButton, QtCore.SIGNAL("clicked()"), Login.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), Login.reject)
        QtCore.QObject.connect(self.usernameValue, QtCore.SIGNAL("returnPressed()"), Login.accept)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameLabel.setText(QtGui.QApplication.translate("Login", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("Login", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Login", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

