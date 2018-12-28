import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import *
from PyQt5 import QtCore

import EVE_Tool


class Ui(EVE_Tool.Ui_MainWindow):  # 继承至父类ui
    def __init__(self):
        self.dbConnect()  # 连接business数据库

    def dbConnect(self):
        db = QSqlDatabase.addDatabase('QSQLITE')  # 数据库类型
        db.setDatabaseName('business.db')  # 数据库名称
        try :
            db.open()
            print("数据库连接成功")
        except:
            print("数据库连接失败")

    def DataShow(self):
        self.model = QSqlTableModel()  # 实例化QSqlTableModel
        self.tableView_resell.setModel(self.model)  # 为tableView_resell（主显示表格）设置模型self.model
        # self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.setTable('resell')  # 指定数据库表格
        self.model.select()  # 查询所有数据
        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'typeID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'typeName')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    ui.DataShow()
    MainWindow.show()
    sys.exit(app.exec_())

