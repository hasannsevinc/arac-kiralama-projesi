from PyQt5.QtWidgets import *
import sys
import sqlite3 as sql
from menuui import Ui_MainWindow
from aracEkleme import aracMenu
from musteriEkleme import Musteri
from kiralamaMenu import Kiralama


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #signal slots
        self.ui.actionKiralama_Menu.triggered.connect(self.kiralama_menu)
        self.ui.actionArac_Menu.triggered.connect(self.arac_menu)
        self.ui.actionMusteri_Menu.triggered.connect(self.musteri_menu)

    def kiralama_menu(self):
        kiralama_penceresi = Kiralama()
        kiralama_penceresi.exec_()

    def arac_menu(self):
        arac_penceresi = aracMenu()
        arac_penceresi.exec_()

    def musteri_menu(self):
        musteri_penceresi = Musteri()
        musteri_penceresi.exec_()


if __name__ == "__main__":
    app = QApplication([])
    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec_())