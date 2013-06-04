# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Tue Jun  4 15:16:08 2013
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(814, 596)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShape(QtGui.QFrame.Box)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_HDD = QtGui.QAction(MainWindow)
        self.actionAdd_HDD.setObjectName("actionAdd_HDD")
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionMake_Backup = QtGui.QAction(MainWindow)
        self.actionMake_Backup.setObjectName("actionMake_Backup")
        self.actionBrowse = QtGui.QAction(MainWindow)
        self.actionBrowse.setObjectName("actionBrowse")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_User = QtGui.QAction(MainWindow)
        self.actionAdd_User.setObjectName("actionAdd_User")
        self.actionDelete_User = QtGui.QAction(MainWindow)
        self.actionDelete_User.setObjectName("actionDelete_User")
        self.actionEdit_User = QtGui.QAction(MainWindow)
        self.actionEdit_User.setObjectName("actionEdit_User")
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menuFile.addAction(self.actionAdd_HDD)
        self.menuFile.addAction(self.actionBrowse)
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionMake_Backup)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionAdd_HDD, QtCore.SIGNAL("triggered()"), MainWindow.add_hard_drive)
        QtCore.QObject.connect(self.actionBrowse, QtCore.SIGNAL("triggered()"), MainWindow.browse)
        QtCore.QObject.connect(self.actionMake_Backup, QtCore.SIGNAL("triggered()"), MainWindow.make_backup)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actionSearch, QtCore.SIGNAL("triggered()"), MainWindow.search)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL("triggered()"), MainWindow.about)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellEntered(int,int)"), MainWindow.drive_selected)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellDoubleClicked(int,int)"), MainWindow.drive_selected)
        QtCore.QObject.connect(self.actionAdd_User, QtCore.SIGNAL("triggered()"), MainWindow.addUser)
        QtCore.QObject.connect(self.actionDelete_User, QtCore.SIGNAL("triggered()"), MainWindow.delUser)
        QtCore.QObject.connect(self.actionEdit_User, QtCore.SIGNAL("triggered()"), MainWindow.editUser)
        QtCore.QObject.connect(self.actionRefresh, QtCore.SIGNAL("triggered()"), MainWindow.refresh)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Copy Station", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Serial", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Drive Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Date Added", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Copies Of", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_HDD.setText(QtGui.QApplication.translate("MainWindow", "&Add Harddrive(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_HDD.setToolTip(QtGui.QApplication.translate("MainWindow", "Add Harddrive(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_HDD.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "&Search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMake_Backup.setText(QtGui.QApplication.translate("MainWindow", "Make Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBrowse.setText(QtGui.QApplication.translate("MainWindow", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBrowse.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_User.setText(QtGui.QApplication.translate("MainWindow", "Add User", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_User.setText(QtGui.QApplication.translate("MainWindow", "Delete User", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_User.setText(QtGui.QApplication.translate("MainWindow", "Edit User", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
