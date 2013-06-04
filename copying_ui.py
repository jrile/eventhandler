# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/copying.ui'
#
# Created: Tue Jun  4 15:15:35 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Copying(object):
    def setupUi(self, Copying):
        Copying.setObjectName("Copying")
        Copying.resize(417, 169)
        self.centralwidget = QtGui.QWidget(Copying)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(20)
        self.progressBar.setProperty("value", 20)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel = QtGui.QPushButton(self.centralwidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Copying.setCentralWidget(self.centralwidget)

        self.retranslateUi(Copying)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL("clicked()"), Copying.reject)
        QtCore.QMetaObject.connectSlotsByName(Copying)

    def retranslateUi(self, Copying):
        Copying.setWindowTitle(QtGui.QApplication.translate("Copying", "Copying", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Copying", "Copying:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Copying", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

