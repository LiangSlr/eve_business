# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EVE_Tool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 679)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName("tabWidget_main")
        self.tab_resell = QtWidgets.QWidget()
        self.tab_resell.setObjectName("tab_resell")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_resell)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_tool = QtWidgets.QGroupBox(self.tab_resell)
        self.groupBox_tool.setTitle("")
        self.groupBox_tool.setObjectName("groupBox_tool")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_tool)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_tool)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_tool)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox_tool)
        self.groupBox_resell = QtWidgets.QGroupBox(self.tab_resell)
        self.groupBox_resell.setTitle("")
        self.groupBox_resell.setObjectName("groupBox_resell")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_resell)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_tree = QtWidgets.QGroupBox(self.groupBox_resell)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_tree.sizePolicy().hasHeightForWidth())
        self.groupBox_tree.setSizePolicy(sizePolicy)
        self.groupBox_tree.setTitle("")
        self.groupBox_tree.setObjectName("groupBox_tree")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_tree)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeView_resell = QtWidgets.QTreeView(self.groupBox_tree)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_resell.sizePolicy().hasHeightForWidth())
        self.treeView_resell.setSizePolicy(sizePolicy)
        self.treeView_resell.setMinimumSize(QtCore.QSize(0, 0))
        self.treeView_resell.setObjectName("treeView_resell")
        self.verticalLayout_5.addWidget(self.treeView_resell)
        self.groupBox_tool_left = QtWidgets.QGroupBox(self.groupBox_tree)
        self.groupBox_tool_left.setTitle("")
        self.groupBox_tool_left.setObjectName("groupBox_tool_left")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_tool_left)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 78, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.groupBox_tool_left)
        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_tree)
        self.splitter = QtWidgets.QSplitter(self.groupBox_resell)
        self.splitter.setLineWidth(5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.tableView_resell = QtWidgets.QTableView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_resell.sizePolicy().hasHeightForWidth())
        self.tableView_resell.setSizePolicy(sizePolicy)
        self.tableView_resell.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView_resell.setObjectName("tableView_resell")
        self.groupBox_type_detail = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_type_detail.setTitle("")
        self.groupBox_type_detail.setObjectName("groupBox_type_detail")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_type_detail)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_type_detail = QtWidgets.QTextBrowser(self.groupBox_type_detail)
        self.textBrowser_type_detail.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser_type_detail.setObjectName("textBrowser_type_detail")
        self.verticalLayout_4.addWidget(self.textBrowser_type_detail)
        self.tabWidget_type_detail = QtWidgets.QTabWidget(self.groupBox_type_detail)
        self.tabWidget_type_detail.setObjectName("tabWidget_type_detail")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_type_detail.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_type_detail.addTab(self.tab_4, "")
        self.verticalLayout_4.addWidget(self.tabWidget_type_detail)
        self.verticalLayout_4.setStretch(0, 20)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.addWidget(self.groupBox_resell)
        self.verticalLayout_2.setStretch(1, 10)
        self.tabWidget_main.addTab(self.tab_resell, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_main.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_main.setCurrentIndex(0)
        self.tabWidget_type_detail.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EVE_Tool"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget_type_detail.setTabText(self.tabWidget_type_detail.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget_type_detail.setTabText(self.tabWidget_type_detail.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_resell), _translate("MainWindow", "Resell"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action3.setText(_translate("MainWindow", "3"))
