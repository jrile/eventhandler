# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/location.ui'
#
# Created: Tue Jun  4 15:15:57 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Location(object):
    def setupUi(self, Location):
        Location.setObjectName("Location")
        Location.resize(305, 269)
        self.verticalLayout = QtGui.QVBoxLayout(Location)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Location)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.locationBox = QtGui.QPlainTextEdit(Location)
        self.locationBox.setObjectName("locationBox")
        self.verticalLayout.addWidget(self.locationBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtGui.QPushButton(Location)
        self.update.setAutoDefault(False)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close = QtGui.QPushButton(Location)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Location)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL("clicked()"), Location.reject)
        QtCore.QObject.connect(self.update, QtCore.SIGNAL("clicked()"), Location.accept)
        QtCore.QMetaObject.connectSlotsByName(Location)

    def retranslateUi(self, Location):
        Location.setWindowTitle(QtGui.QApplication.translate("Location", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.update.setText(QtGui.QApplication.translate("Location", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Location", "Close", None, QtGui.QApplication.UnicodeUTF8))

