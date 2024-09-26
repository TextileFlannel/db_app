from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from controllers.main_controller import MainController
from PyQt5 import uic
from database.models import User


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.controller = MainController(self)
        self.pushButton.clicked.connect(self.add_data)
        self.pushButton_2.clicked.connect(self.del_data)
        self.pushButton_3.clicked.connect(self.clear_filter)
        self.pushButton_4.clicked.connect(self.filter_data)

    def add_data(self):
        name = self.lineEdit.text()
        age = int(self.spinBox.value())
        email = self.lineEdit_2.text()
        self.controller.add_user(name, age, email)

    def del_data(self):
        row = self.tableWidget.currentRow()
        if row != -1:
            item = self.tableWidget.item(row, 0)
            self.controller.del_user(item)

    def clear_filter(self):
        self.controller.load_user()

    def filter_data(self):
        ageAt = self.spinBox_2.value()
        ageTo = self.spinBox_3.value()
        fname = self.checkBox_2.isChecked()
        fage = self.checkBox.isChecked()
        self.controller.filter_user(ageAt, ageTo, fname, fage)

    def display_user(self, users):
        columns = User.__table__.columns.keys()
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.setRowCount(len(users))
        for row, user in enumerate(users):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(user.id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(user.name))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(user.age)))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(user.email))
