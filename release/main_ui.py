# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 498)
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(10, 10, 671, 421))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.change_data_btn = QtWidgets.QPushButton(Form)
        self.change_data_btn.setGeometry(QtCore.QRect(10, 470, 131, 23))
        self.change_data_btn.setObjectName("change_data_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.change_data_btn.setText(_translate("Form", "Редактировать данные"))
