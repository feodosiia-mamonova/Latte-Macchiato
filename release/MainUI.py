# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addCoffeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.addCoffeeButton.setGeometry(QtCore.QRect(20, 440, 151, 23))
        self.addCoffeeButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.editCoffeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.editCoffeeButton.setGeometry(QtCore.QRect(20, 470, 151, 23))
        self.editCoffeeButton.setObjectName("pushButton")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.filmsTable = QTableWidget(self)
        self.filmsTable.setGeometry(QtCore.QRect(20, 20, 511, 411))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addCoffeeButton.setText(_translate("MainWindow", "Добавить данные"))
        self.editCoffeeButton.setText(_translate("MainWindow", "Изменить данные данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

