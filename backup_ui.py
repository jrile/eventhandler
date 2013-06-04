# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/backup.ui'
#
# Created: Tue Jun  4 15:15:24 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BackupHDD(object):
    def setupUi(self, BackupHDD):
        BackupHDD.setObjectName("BackupHDD")
        BackupHDD.resize(362, 303)
        self.verticalLayout = QtGui.QVBoxLayout(BackupHDD)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backupTable = QtGui.QTableWidget(BackupHDD)
        self.backupTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.backupTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.backupTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.backupTable.setObjectName("backupTable")
        self.backupTable.setColumnCount(2)
        self.backupTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.backupTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.backupTable.setHorizontalHeaderItem(1, item)
        self.backupTable.horizontalHeader().setVisible(False)
        self.backupTable.horizontalHeader().setCascadingSectionResizes(True)
        self.backupTable.verticalHeader().setVisible(False)
        self.backupTable.verticalHeader().setCascadingSectionResizes(True)
        self.backupTable.verticalHeader().setDefaultSectionSize(40)
        self.backupTable.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout.addWidget(self.backupTable)
        self.buttonBox = QtGui.QDialogButtonBox(BackupHDD)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BackupHDD)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), BackupHDD.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BackupHDD.reject)
        QtCore.QMetaObject.connectSlotsByName(BackupHDD)

    def retranslateUi(self, BackupHDD):
        BackupHDD.setWindowTitle(QtGui.QApplication.translate("BackupHDD", "Backup Files", None, QtGui.QApplication.UnicodeUTF8))
        self.backupTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("BackupHDD", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.backupTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("BackupHDD", "Destination", None, QtGui.QApplication.UnicodeUTF8))

