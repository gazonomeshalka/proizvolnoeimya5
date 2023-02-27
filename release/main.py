import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_Form
from addEditCoffeeForm import Ui_Form as Ui_Add


def change(window):
    global exx
    window.setEnabled(False)

    class ChangeWindow(QWidget, Ui_Add):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.str_del_btn.clicked.connect(self.delt)
            self.upd_btn.clicked.connect(self.upd)
            self.new_btn.clicked.connect(self.new)
            v = ['название сорта', 'степень обжарки', 'молотый или в зернах',
                 'описание вкуса', 'цена', 'объём упаковки']
            for item in v:
                self.type_upd.addItem(item)

        def terminate(self):
            self.hide()
            window.loadTable()
            window.setEnabled(True)
            return

        def delt(self):
            bd = sqlite3.connect('coffee.sqlite')
            cur = bd.cursor()
            value = self.str_del_id.value()
            cur.execute(f"""DELETE from coffee where ID == {value}""")
            bd.commit()
            bd.close()
            self.terminate()

        def upd(self):
            id = self.str_upd_id.value()
            t = self.type_upd.currentText()
            new_value = self.new_type_val_upd.text()
            bd = sqlite3.connect('coffee.sqlite')
            cur = bd.cursor()
            cur.execute(f"""UPDATE coffee SET "{t}" = "{new_value}" WHERE ID == {id}""")
            bd.commit()
            bd.close()
            self.terminate()

        def new(self):
            one = ('("название сорта", "степень обжарки", "молотый или в зернах", ' +
                   '"описание вкуса", "цена", "объём упаковки")')
            values = [self.new_sort.text(), self.new_obzh.text(), str(self.new_mol_vz.value()),
                      self.new_taste.text(), str(self.new_price.value()), str(self.new_size.value())]
            values = ['"' + e + '"' for e in values]
            two = '(' + ', '.join(values) + ')'
            bd = sqlite3.connect('coffee.sqlite')
            cur = bd.cursor()
            cur.execute(f"""INSERT INTO coffee {one} VALUES {two}""")
            bd.commit()
            bd.close()
            self.terminate()

    exx = ChangeWindow()
    exx.show()


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable()
        self.change_data_btn.clicked.connect(self.change_data)
        self.r = 0

    def loadTable(self):
        self.table.clear()
        bd = sqlite3.connect('coffee.sqlite')
        cur = bd.cursor()
        self.table.setRowCount(0)
        data = cur.execute("""SELECT * from coffee""").fetchall()
        self.table.setColumnCount(len(data[0]))
        for i in range(len(data)):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j in range(len(data[0])):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(data[i][j])))
        self.table.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                              'молотый/в зернах', 'описание вкуса', 'цена',
                                              'объём упаковки'])
        bd.close()

    def change_data(self):
        change(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
