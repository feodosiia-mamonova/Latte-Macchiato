import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from MainUI import Ui_MainWindow
from addEditCoffeeForm import Ui_ADDWindow

DB_NAME = "coffee.db"


class AddFilmWidget(QMainWindow, Ui_ADDWindow):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        self.setupUi(self)
        self.flag = False
        self.film_id = film_id
        if film_id is not None:
            self.pushButton.clicked.connect(self.edit_elem)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            self.get_elem()

        else:
            self.pushButton.clicked.connect(self.add_elem)

    def get_elem(self):
        cur = self.con.cursor()
        item = cur.execute(
            f"SELECT c.id, c.variety, c.roasting, c.ground_or_grains, c.taste, c.price, "
            f"c.volume FROM coffee as c").fetchone()
        self.variety.setPlainText(item[1])
        self.roasting.setPlainText(str(item[2]))
        self.ground_or_grains.setPlainText(str(item[3]))
        self.taste.setPlainText(str(item[4]))
        self.price.setPlainText(str(item[5]))
        self.volume.setPlainText(str(item[6]))

    def selectGenres(self):
        pass

    def add_elem(self):
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM coffee").fetchone()[0]
            new_data = (id_off + 1, self.variety.toPlainText(), self.roasting.toPlainText(),
                        self.ground_or_grains.toPlainText(), self.taste.toPlainText(),
                        int(self.price.toPlainText()), int(self.volume.toPlainText()))
            cur.execute("INSERT INTO coffee VALUES (?,?,?,?,?,?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_films()
            self.close()

    def edit_elem(self):
        cur = self.con.cursor()
        try:
            new_data = (self.variety.toPlainText(), self.roasting.toPlainText(),
                        self.ground_or_grains.toPlainText(), self.taste.toPlainText(),
                        int(self.price.toPlainText()), int(self.volume.toPlainText()), self.film_id)
            cur.execute("UPDATE coffee SET variety=?, roasting=?, ground_or_grains=?, taste=?, price=?, volume=? "
                        "WHERE id=?", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_films()
            self.close()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.con = sqlite3.connect(DB_NAME)
        self.update_films()
        self.addCoffeeButton.clicked.connect(self.add_film)
        self.editCoffeeButton.clicked.connect(self.edit_film)
        self.dialogs = list()

    def update_films(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        que = "SELECT c.id, c.variety, c.roasting, c.ground_or_grains, c.taste, c.price, c.volume FROM coffee as c"
        result = cur.execute(que).fetchall()
        self.filmsTable.setRowCount(len(result))
        self.filmsTable.setColumnCount(len(result[0]))
        self.filmsTable.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки',
             'Молотый/в зернах', 'Вкус', 'Цена', 'Объем'])

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.filmsTable.setItem(i, j, QTableWidgetItem(str(val)))

    def add_film(self):
        dialog = AddFilmWidget(self)
        dialog.show()

    def edit_film(self):
        rows = list(set([i.row() for i in self.filmsTable.selectedItems()]))
        ids = [self.filmsTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddFilmWidget(self, film_id=ids[0])
        dialog.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
