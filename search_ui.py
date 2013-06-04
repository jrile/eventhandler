# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/search.ui'
#
# Created: Tue Jun  4 15:40:02 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 315)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.serial = QtGui.QLineEdit(Dialog)
        self.serial.setObjectName("serial")
        self.gridLayout.addWidget(self.serial, 0, 1, 1, 1)
        self.drive_name_2 = QtGui.QLabel(Dialog)
        self.drive_name_2.setObjectName("drive_name_2")
        self.gridLayout.addWidget(self.drive_name_2, 1, 0, 1, 1)
        self.drive_name = QtGui.QLineEdit(Dialog)
        self.drive_name.setObjectName("drive_name")
        self.gridLayout.addWidget(self.drive_name, 1, 1, 1, 1)
        self.date_check = QtGui.QCheckBox(Dialog)
        self.date_check.setObjectName("date_check")
        self.gridLayout.addWidget(self.date_check, 3, 0, 1, 1)
        self.before = QtGui.QDateEdit(Dialog)
        self.before.setObjectName("before")
        self.gridLayout.addWidget(self.before, 3, 1, 1, 1)
        self.after = QtGui.QDateEdit(Dialog)
        self.after.setObjectName("after")
        self.gridLayout.addWidget(self.after, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.filename = QtGui.QLineEdit(Dialog)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Serial:", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_name_2.setText(QtGui.QApplication.translate("Dialog", "Drive Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.date_check.setText(QtGui.QApplication.translate("Dialog", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Filename:", None, QtGui.QApplication.UnicodeUTF8))

