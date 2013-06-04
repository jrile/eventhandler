# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/select.ui'
#
# Created: Tue Jun  4 15:16:15 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectHDD(object):
    def setupUi(self, SelectHDD):
        SelectHDD.setObjectName("SelectHDD")
        SelectHDD.resize(240, 325)
        self.verticalLayout = QtGui.QVBoxLayout(SelectHDD)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hddList = QtGui.QListWidget(SelectHDD)
        self.hddList.setAlternatingRowColors(True)
        self.hddList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.hddList.setResizeMode(QtGui.QListView.Adjust)
        self.hddList.setSpacing(5)
        self.hddList.setObjectName("hddList")
        self.verticalLayout.addWidget(self.hddList)
        self.buttonBox = QtGui.QDialogButtonBox(SelectHDD)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectHDD)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SelectHDD.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SelectHDD.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectHDD)

    def retranslateUi(self, SelectHDD):
        SelectHDD.setWindowTitle(QtGui.QApplication.translate("SelectHDD", "Select harddrives:", None, QtGui.QApplication.UnicodeUTF8))

