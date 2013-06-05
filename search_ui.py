# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/search.ui'
#
# Created: Wed Jun  5 08:18:20 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(502, 315)
        self.verticalLayout = QtGui.QVBoxLayout(Search)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Search)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.serial = QtGui.QLineEdit(Search)
        self.serial.setMaxLength(30)
        self.serial.setObjectName("serial")
        self.gridLayout.addWidget(self.serial, 0, 1, 1, 1)
        self.drive_name_2 = QtGui.QLabel(Search)
        self.drive_name_2.setObjectName("drive_name_2")
        self.gridLayout.addWidget(self.drive_name_2, 1, 0, 1, 1)
        self.drive_name = QtGui.QLineEdit(Search)
        self.drive_name.setMaxLength(50)
        self.drive_name.setObjectName("drive_name")
        self.gridLayout.addWidget(self.drive_name, 1, 1, 1, 1)
        self.date_check = QtGui.QCheckBox(Search)
        self.date_check.setChecked(False)
        self.date_check.setObjectName("date_check")
        self.gridLayout.addWidget(self.date_check, 3, 0, 1, 1)
        self.before = QtGui.QDateEdit(Search)
        self.before.setObjectName("before")
        self.gridLayout.addWidget(self.before, 3, 1, 1, 1)
        self.after = QtGui.QDateEdit(Search)
        self.after.setObjectName("after")
        self.gridLayout.addWidget(self.after, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Search)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.username = QtGui.QLineEdit(Search)
        self.username.setMaxLength(20)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Search)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.filename = QtGui.QLineEdit(Search)
        self.filename.setMaxLength(100)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Search)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Search)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Search.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Search.reject)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        Search.setWindowTitle(QtGui.QApplication.translate("Search", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Search", "Serial:", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_name_2.setText(QtGui.QApplication.translate("Search", "Drive Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.date_check.setText(QtGui.QApplication.translate("Search", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Search", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Search", "Filename:", None, QtGui.QApplication.UnicodeUTF8))

