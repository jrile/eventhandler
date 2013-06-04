# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/delete_user.ui'
#
# Created: Tue Jun  4 15:46:05 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DelUser(object):
    def setupUi(self, DelUser):
        DelUser.setObjectName("DelUser")
        DelUser.resize(311, 133)
        self.verticalLayout = QtGui.QVBoxLayout(DelUser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(DelUser)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username = QtGui.QLineEdit(DelUser)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DelUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DelUser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DelUser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DelUser.reject)
        QtCore.QMetaObject.connectSlotsByName(DelUser)

    def retranslateUi(self, DelUser):
        DelUser.setWindowTitle(QtGui.QApplication.translate("DelUser", "Delete User", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DelUser", "Username:", None, QtGui.QApplication.UnicodeUTF8))

