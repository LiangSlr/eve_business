import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import *
from PyQt5 import QtCore

import EVE_Tool

class Ui(EVE_Tool.Ui_MainWindow):  # 继承至父类ui
    def __init__(self):
        super().__init__()  # 超继承父类
        self.setupUi(MainWindow)  # 初始化父类设置，即初始化ui设置
        self.dbConnect()  # 连接business数据库
        self.dataShow()  # 显示数据
        self.tableSet()  # 调整数据表格格式
        self.treeSet()  # 树图与数据表之间的信号/槽连接

    def dbConnect(self):
        db = QSqlDatabase.addDatabase('QSQLITE')  # 数据库类型
        db.setDatabaseName('business.db')  # 数据库名称
        try :
            db.open()
            print("数据库连接成功")
        except:
            print("数据库连接失败")

    def tableSet(self):
        """表格属性设置"""
        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'typeID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'typeName')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Jita')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'Domain')
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, 'Margin')
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, 'Ten thousands')
        # 调整列宽
        self.tableView_resell.resizeColumnToContents(0)
        self.tableView_resell.setColumnWidth(2, 60)
        self.tableView_resell.resizeColumnToContents(3)

    def dataShow(self):
        self.model = QSqlTableModel()  # 实例化QSqlTableModel
        self.tableView_resell.setModel(self.model)  # 为tableView_resell（主显示表格）设置模型self.model
        # self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # 允许字段更改,允许更改表格内容
        self.model.setTable('resell')  # 指定数据库表格
        self.model.select()  # 查询所有数据
        self.tableView_resell.setColumnHidden(2, 1)
        # 排序,直接开启所有列的排序功能
        self.tableView_resell.setSortingEnabled(1)
        self.tableView_resell.sortByColumn(6, 1)


    def rowHidden(self):
        """隐藏不需要的内容"""
        print('test')
        self.tableView_resell.setRowHidden(1, 1)

    def treeSet(self):
        """tree与table之间的连接（信号/槽）"""
        print('selectionMode true')
        self.treeWidget_resell.itemClicked['QTreeWidgetItem*', 'int'].connect(self.rowHidden)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui()
    MainWindow.show()
    sys.exit(app.exec_())

