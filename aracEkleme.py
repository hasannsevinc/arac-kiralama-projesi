from PyQt5.QtWidgets import *
import sys
import sqlite3 as sql
from aracEklemeui import Ui_Dialog

class aracMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #table widgetta satırı tutucak
        self.curRowIndex = 0

        # SQLite bağlantısı
        self.conn = sql.connect('database.db')
        self.cur = self.conn.cursor()

        # Araç plaka eklemeye focus
        self.ui.ekleme_plaka_text.setFocus()

        # Signal-slot bağlantıları
        self.ui.ekleme_button_EKLE.clicked.connect(self.ekleme)
        self.ui.ekleme_button_YENI.clicked.connect(self.yeni)
        self.ui.araclar_sag_ilerle.clicked.connect(self.Sonraki)
        self.ui.araclar_sol_ilerle.clicked.connect(self.Onceki)
        self.ui.tableWidget.itemSelectionChanged.connect(self.SelectedIndexChanged)  # satır indexi değişirse
        self.ui.ekleme_button_sil.clicked.connect(self.sil)
        self.ui.ekleme_button_Duzenle.clicked.connect(self.duzenle)
        self.ui.ekleme_button_cikis.clicked.connect(self.cikis)

        #uygulama çalıştığında otomatik kayitli tablolar gelir
        self.comboBox()
        self.tableWidgetGoster()

    def SelectedIndexChanged(self): # table üzerinden satırlara dokunduğumda tetiklenicek

        indeks = self.ui.tableWidget.currentIndex()  # PyQt5.QtCore.QModelIndex türünde nesne döndürür
        self.curRowIndex = indeks.row()  # bu nesnenin row() metodu ile satır index'i elde ediliyor
        self.ui.tableWidget.setCurrentCell(self.curRowIndex, 0)
        self.TableWidgettoForm() # seçili satır boş text ekranlarına gelicek

    def Sonraki(self):
        print("Sonraki Butonuna tıklandı")
        self.curRowIndex += 1  # kayıt indeksini bir artır
        if self.curRowIndex == self.ui.tableWidget.rowCount():  # kayıt sayısı aşılmıssa ilk kayda git
            self.curRowIndex = 0
        self.ui.tableWidget.setCurrentCell(self.curRowIndex,0)  # curRowIndex'inci satıra ve 0. sütuna git. (row,col) --- hatalı

    def Onceki(self):
        print("Önceki Butonuna tıklandı")
        self.curRowIndex -= 1
        if (self.curRowIndex < 0):
            self.curRowIndex = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setCurrentCell(self.curRowIndex, 0)


    def TableWidgettoForm(self): # seçili curRow sayesinde satırdaki veriler formlara aktarılır
        selectedRowItem = self.ui.tableWidget.selectedItems();  # tableWidget1 SelectionBehavior özelliği SelectRows olmalıdır. Aksi halde seçili olan hücre sadece gelir.
        self.ui.ekleme_plaka_text.setText(selectedRowItem[1].text())
        self.ui.ekleme_marka_text.setText(selectedRowItem[2].text())
        self.ui.ekleme_model_text.setText(selectedRowItem[3].text())
        self.ui.ekleme_yil_text.setText(selectedRowItem[4].text())
    def ekleme(self):
        plaka = self.ui.ekleme_plaka_text.text()
        marka = self.ui.ekleme_marka_text.text()
        model = self.ui.ekleme_model_text.text()
        yil = self.ui.ekleme_yil_text.text()


        if plaka != '' and marka != '' and model != '' and yil != '':
            sql1 = "INSERT INTO ARACLAR (ARAC_PLAKA, ARAC_MARKA, ARAC_MODEL, ARAC_YIL) VALUES (?, ?, ?, ?)"
            params = (plaka, marka, model, yil)

            self.cur.execute(sql1, params)
            self.conn.commit()
            QMessageBox.information(self, "Bilgilendirme", "Kaydınız başarıyla eklendi")
            self.yeni()
            self.tableWidgetGoster()
        else:
            QMessageBox.information(self, "Bilgilendirme", "Lutfen Tum Alanları Doldurunuz")

    def sil(self):
        response = QMessageBox.question(self, "Silme Onay", "Seçili kaydı silmek istediğinize emin misiniz?",
                                        QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            # Seçili satırın ARAC_ID'sini al
            arac_id = self.ui.tableWidget.item(self.curRowIndex,0).text()  # Örneğin, ARAC_ID'nin 0. sütunda olduğunu varsayalım

            # Veritabanından kaydı sil
            self.cur.execute("DELETE FROM ARACLAR WHERE ARAC_ID = ?", (arac_id,))
            self.conn.commit()

            self.tableWidgetGoster()

    def duzenle(self):
        plaka = self.ui.ekleme_plaka_text.text()
        marka = self.ui.ekleme_marka_text.text()
        model = self.ui.ekleme_model_text.text()
        yil = self.ui.ekleme_yil_text.text()

        arac_id = self.ui.tableWidget.item(self.curRowIndex, 0).text()

        sql = "UPDATE ARACLAR SET ARAC_PLAKA = ?, ARAC_MARKA = ?, ARAC_MODEL = ?, ARAC_YIL = ? WHERE ARAC_ID = ?"
        params = (plaka, marka, model, yil, arac_id)

        self.cur.execute(sql, params)
        self.conn.commit()
        self.tableWidgetGoster()
        QMessageBox.information(self, 'Bilgilendirme', 'Kayit Basariyla Düzeltilmiştir')

    def tableWidgetGoster(self):
        sql1 = "SELECT * FROM ARACLAR"
        veriler = list(self.cur.execute(sql1))  # veri çekiliyor ve list veri tipine çevriliyor
        print(veriler)
        rowcount = len(veriler)  # kayıt sayısı elde ediliyor
        kayitSayi = 0
        self.ui.tableWidget.setRowCount(rowcount)
        for rowindex, rowdata in enumerate(veriler):  # sorgudan dönen satırlar (list row)
            for colindex, coldata in enumerate(rowdata):  # sorgudan elde edilen sütun verisi
                self.ui.tableWidget.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
            kayitSayi+=1
        self.ui.kayitsayisiLabel.setText(f"{kayitSayi}")


    def yeni(self):
        # Yeni butonuna tıkladığında metin kutularını temizleme ve plaka metin kutusuna odaklanma
        self.ui.ekleme_marka_text.setText('')
        self.ui.ekleme_model_text.setText('')
        self.ui.ekleme_yil_text.setText('')
        self.ui.ekleme_plaka_text.setText('')
        self.ui.ekleme_plaka_text.setFocus()

    def comboBox(self):  # comboBox'a göre listeleme yapamadım cunku aynı marka bir den fazla ekleniyordu
        sql1 = "SELECT * FROM ARACLAR"
        veriler = list(self.cur.execute(sql1))
        markalar = []

        for i in veriler:
            markalar.append(i[2])


        for index, item in enumerate(markalar):
            self.ui.araclarComboBox.insertItem(index,item) #index- marka


    def cikis(self):
        pencere.close()

if __name__ == "__main__":
    app = QApplication([])
    pencere = aracMenu()
    pencere.show()
    sys.exit(app.exec_())
