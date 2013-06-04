# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/folder_view.ui'
#
# Created: Tue Jun  4 15:15:48 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FolderView(object):
    def setupUi(self, FolderView):
        FolderView.setObjectName("FolderView")
        FolderView.resize(640, 472)
        self.verticalLayout = QtGui.QVBoxLayout(FolderView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.folder = QtGui.QTreeWidget(FolderView)
        self.folder.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.folder.setAlternatingRowColors(False)
        self.folder.setObjectName("folder")
        self.folder.header().setVisible(False)
        self.verticalLayout.addWidget(self.folder)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.copyLabel = QtGui.QLabel(FolderView)
        self.copyLabel.setObjectName("copyLabel")
        self.horizontalLayout.addWidget(self.copyLabel)
        self.location = QtGui.QPushButton(FolderView)
        self.location.setObjectName("location")
        self.horizontalLayout.addWidget(self.location)
        self.okay = QtGui.QPushButton(FolderView)
        self.okay.setObjectName("okay")
        self.horizontalLayout.addWidget(self.okay)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(FolderView)
        QtCore.QObject.connect(self.okay, QtCore.SIGNAL("clicked()"), FolderView.accept)
        QtCore.QObject.connect(self.location, QtCore.SIGNAL("clicked()"), FolderView.location)
        QtCore.QMetaObject.connectSlotsByName(FolderView)

    def retranslateUi(self, FolderView):
        FolderView.setWindowTitle(QtGui.QApplication.translate("FolderView", "Drive View", None, QtGui.QApplication.UnicodeUTF8))
        self.copyLabel.setText(QtGui.QApplication.translate("FolderView", "# copies: ", None, QtGui.QApplication.UnicodeUTF8))
        self.location.setText(QtGui.QApplication.translate("FolderView", "View/Edit Location", None, QtGui.QApplication.UnicodeUTF8))
        self.okay.setText(QtGui.QApplication.translate("FolderView", "Close", None, QtGui.QApplication.UnicodeUTF8))

