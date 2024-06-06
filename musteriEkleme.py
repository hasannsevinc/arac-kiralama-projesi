from PyQt5.QtWidgets import *
import sys
import sqlite3 as sql
from musteriEklemeui import Ui_Dialog


class Musteri(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # table widgetta satırı tutucak
        self.curRowIndex = 0

        # Musteri TC eklemeye focus
        self.ui.ekleme_tc_text.setFocus()

        # sqlite baglantısı
        self.conn = sql.connect('database.db')
        self.cur = self.conn.cursor()

        # Signal-slot bağlantıları
        self.ui.ekleme_button_ekle.clicked.connect(self.ekleme)
        self.ui.ekleme_button_yeni.clicked.connect(self.yeni)
        self.ui.musteriler_sag.clicked.connect(self.Sonraki)
        self.ui.musteriler_sol.clicked.connect(self.Onceki)
        self.ui.musteriTablo.itemSelectionChanged.connect(self.SelectedIndexChanged)  # satır indexi değişirse
        self.ui.ekleme_button_sil.clicked.connect(self.sil)
        self.ui.ekleme_button_duzenle.clicked.connect(self.duzenle)
        self.ui.ekleme_button_cikis.clicked.connect(self.cikis)

        # uygulama çalıştığında otomatik kayitli tablolar gelir
        self.tableWidgetGoster()

    def SelectedIndexChanged(self):  # table üzerinden satırlara dokunduğumda tetiklenicek
        indeks = self.ui.musteriTablo.currentIndex()  # PyQt5.QtCore.QModelIndex türünde nesne döndürür
        self.curRowIndex = indeks.row()  # bu nesnenin row() metodu ile satır index'i elde ediliyor
        self.ui.musteriTablo.setCurrentCell(self.curRowIndex, 0)
        self.TableWidgettoForm()  # seçili satır boş text ekranlarına gelicek

    def Sonraki(self):
        print("Sonraki Butonuna tıklandı")
        self.curRowIndex += 1  # kayıt indeksini bir artır
        if self.curRowIndex == self.ui.musteriTablo.rowCount():  # kayıt sayısı aşılmıssa ilk kayda git
            self.curRowIndex = 0
        self.ui.musteriTablo.setCurrentCell(self.curRowIndex, 0)  # curRowIndex'inci satıra ve 0. sütuna git. (row, col) --- hatalı

    def Onceki(self):
        print("Önceki Butonuna tıklandı")
        self.curRowIndex -= 1
        if self.curRowIndex < 0:
            self.curRowIndex = self.ui.musteriTablo.rowCount() - 1
        self.ui.musteriTablo.setCurrentCell(self.curRowIndex, 0)

    def TableWidgettoForm(self):  # seçili curRow sayesinde satırdaki veriler formlara aktarılır
        selectedRowItem = self.ui.musteriTablo.selectedItems()  # tableWidget1 SelectionBehavior özelliği SelectRows olmalıdır. Aksi halde seçili olan hücre sadece gelir.
        if selectedRowItem:  # check if there's any selected row
            self.ui.ekleme_tc_text.setText(selectedRowItem[1].text())
            self.ui.ekleme_ad_text.setText(selectedRowItem[2].text())
            self.ui.ekleme_soyad_text.setText(selectedRowItem[3].text())
            self.ui.ekleme_tel_text.setText(selectedRowItem[4].text())

    def tableWidgetGoster(self):
        sql1 = "SELECT * FROM MUSTERILER"
        veriler = list(self.cur.execute(sql1))  # veri çekiliyor ve list veri tipine çevriliyor
        print(veriler)
        rowcount = len(veriler)  # kayıt sayısı elde ediliyor
        kayitSayi = 0
        self.ui.musteriTablo.setRowCount(rowcount)
        for rowindex, rowdata in enumerate(veriler):  # sorgudan dönen satırlar (list row)
            for colindex, coldata in enumerate(rowdata):  # sorgudan elde edilen sütun verisi
                self.ui.musteriTablo.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
            kayitSayi += 1
        self.ui.label_kayit_Sayisi.setText(f"{kayitSayi}")

    def ekleme(self):
        tc = self.ui.ekleme_tc_text.text()
        ad = self.ui.ekleme_ad_text.text()
        soyad = self.ui.ekleme_soyad_text.text()
        tel = self.ui.ekleme_tel_text.text()

        if tc != '' and ad != '' and soyad != '' and tel != '':
            sql1 = "INSERT INTO MUSTERILER (MUSTERI_TC,MUSTERI_NAME,MUSTERI_SURNAME,MUSTERI_TEL) VALUES (?, ?, ?, ?)"
            params = (tc, ad, soyad, tel)

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
            musteri_id = self.ui.musteriTablo.item(self.curRowIndex,0).text()  # Örneğin, ARAC_ID'nin 0. sütunda olduğunu varsayalım

            # Veritabanından kaydı sil
            self.cur.execute("DELETE FROM MUSTERILER WHERE MUSTERI_ID = ?", (musteri_id,))
            self.conn.commit()
            QMessageBox.information(self, "Bilgilendirme", "Kaydınız Başarıyla Silinmiştir")
            self.tableWidgetGoster()
    def duzenle(self):
        tc = self.ui.ekleme_tc_text.text()
        ad = self.ui.ekleme_ad_text.text()
        soyad = self.ui.ekleme_soyad_text.text()
        tel = self.ui.ekleme_tel_text.text()

        musteri_id= self.ui.tableWidget.item(self.curRowIndex, 0).text()

        sql = "UPDATE MUSTERILER SET MUSTERI_TC = ?, MUSTERI_NAME = ?, MUSTERI_SURNAME = ?, MUSTERI_TEL = ? WHERE MUSTERI_ID = ?"
        params = (tc,ad,soyad,tel,musteri_id)

        self.cur.execute(sql, params)
        self.conn.commit()
        self.tableWidgetGoster()
        QMessageBox.information(self, 'Bilgilendirme', 'Kayit Basariyla Düzeltilmiştir')

    def yeni(self):
        # Yeni butonuna tıkladığında metin kutularını temizleme ve plaka metin kutusuna odaklanma
        self.ui.ekleme_tc_text.setText('')
        self.ui.ekleme_ad_text.setText('')
        self.ui.ekleme_soyad_text.setText('')
        self.ui.ekleme_tel_text.setText('')

    def cikis(self):
        pencere.close()


if __name__ == "__main__":
    app = QApplication([])
    pencere = Musteri()
    pencere.show()
    sys.exit(app.exec_())