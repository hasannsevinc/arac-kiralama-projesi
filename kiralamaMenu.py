from PyQt5.QtWidgets import *
import sys
import sqlite3
from kiralamaMenuui import Ui_Dialog


class Kiralama(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # SQLite bağlantısı
        self.conn = sqlite3.connect('database.db')  # Veritabanı dosyasının adı ve uzantısı kontrol edilmeli
        self.cur = self.conn.cursor()

        # table widgetta satırı tutucak
        self.curRowIndex = 0


        # signal slots
        self.ui.kiralama_button_ekle.clicked.connect(self.ekle)
        self.ui.kiralama_button_yeni.clicked.connect(self.yeni)
        self.ui.kiralama_button_sil.clicked.connect(self.sil)
        self.ui.kiralama_button_duzenle.clicked.connect(self.duzenle)
        self.ui.pushButton_Cikis.clicked.connect(self.cikis)

        # Tabloları otomatik olarak getirme
        self.tableWidgetGosterArac()  # Araçlar tablosunu getirir
        self.tableWidgetGosterMusteri()
        self.tableWidgetKiralama()

        # Radio button'lar
        self.ui.aracRadioButton_tumListe.toggled.connect(self.radioButtonStateChanged)
        self.ui.arac_RadioButton_bos.toggled.connect(self.radioButtonStateChanged)

    def tableWidgetRadioButton(self, sql, params):
        veriler = list(self.cur.execute(sql, params))
        print(veriler)
        rowcount = len(veriler)
        kayitSayi = 0
        self.ui.tableWidget_Araclar.setRowCount(rowcount)
        for rowindex, rowdata in enumerate(veriler):  # Sorgudan dönen satırlar (list row)
            for colindex, coldata in enumerate(rowdata):  # Sorgudan elde edilen sütun verisi
                self.ui.tableWidget_Araclar.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
            kayitSayi += 1
        self.ui.label_Arac_kayitSayisi.setText(f"{kayitSayi}")

    def tableWidgetGosterMusteri(self):
        sql1 = "SELECT * FROM MUSTERILER"
        veriler = list(self.cur.execute(sql1))  # Veri çekiliyor ve list veri tipine çevriliyor
        print(veriler)
        rowcount = len(veriler)  # Kayıt sayısı elde ediliyor
        kayitSayi = 0
        self.ui.tableWidget_Musteri.setRowCount(rowcount)
        for rowindex, rowdata in enumerate(veriler):  # Sorgudan dönen satırlar (list row)
            for colindex, coldata in enumerate(rowdata):  # Sorgudan elde edilen sütun verisi
                self.ui.tableWidget_Musteri.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
            kayitSayi += 1
        self.ui.label_musteri_kayitSayi.setText(f"{kayitSayi}")
    def tableWidgetGosterArac(self):
        sql1 = "SELECT * FROM ARACLAR"
        veriler = list(self.cur.execute(sql1))  # Veri çekiliyor ve list veri tipine çevriliyor
        print(veriler)
        rowcount = len(veriler)  # Kayıt sayısı elde ediliyor
        kayitSayi = 0
        self.ui.tableWidget_Araclar.setRowCount(rowcount)
        for rowindex, rowdata in enumerate(veriler):  # Sorgudan dönen satırlar (list row)
            for colindex, coldata in enumerate(rowdata):  # Sorgudan elde edilen sütun verisi
                self.ui.tableWidget_Araclar.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
            kayitSayi += 1
        self.ui.label_Arac_kayitSayisi.setText(f"{kayitSayi}")

    def radioButtonStateChanged(self):  # radio button komutları
        if self.ui.aracRadioButton_tumListe.isChecked():
            self.tableWidgetGosterArac()
        elif self.ui.arac_RadioButton_bos.isChecked():
            sql = "SELECT * FROM ARACLAR WHERE ARAC_DURUM = ?"
            params = ['BOS']
            self.tableWidgetRadioButton(sql, params)

    def tableWidgetKiralama(self):
        # SQL sorgusu
        sql = """
            SELECT k.KIRA_ID, m.MUSTERI_NAME, m.MUSTERI_SURNAME, a.ARAC_PLAKA, a.ARAC_MARKA, k.KIRA_BASLA, k.KIRA_BITIS
            FROM ARACLAR as a
            JOIN KIRA as k ON a.ARAC_ID = k.ARAC_ID
            JOIN MUSTERILER as m ON k.MUSTERI_ID = m.MUSTERI_ID
        """

        # Sorguyu çalıştır
        self.cur.execute(sql)
        results = self.cur.fetchall()

        # Tablonun satır sayısını ayarla
        self.ui.tableWidget_Kiralama.setRowCount(len(results))

        # Verileri tabloya ekle
        for row_index, row_data in enumerate(results):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.ui.tableWidget_Kiralama.setItem(row_index, col_index, item)

    def ekle(self):

        arac_id = self.ui.kiralama_aracId_text.text()
        musteri_id = self.ui.kiralama_musteriId_text.text()
        baslangic = self.ui.kiralama_baslangic_text.text()
        bitis = self.ui.kiralama_bitis_text.text()
        durum = self.ui.kiralama_kiraDurumu_text.text()

        if arac_id != '' and musteri_id != '' and baslangic != '' and bitis != '' and durum != '':
            sql = 'INSERT INTO KIRA (MUSTERI_ID, ARAC_ID, KIRA_BASLA, KIRA_BITIS) VALUES (?, ?, ?, ?)'
            params = [musteri_id, arac_id, baslangic, bitis]
            self.cur.execute(sql, params)
            self.cur.execute('UPDATE ARACLAR SET ARAC_DURUM = ? WHERE ARAC_ID = ?', [durum, arac_id])
            self.conn.commit()
            QMessageBox.information(self, 'Bilgilendirme', 'Kayıtlar başarıyla eklenmiştir')
        else:
            QMessageBox.information(self, 'Bilgilendirme', 'Lütfen tüm boşlukları doldurunuz')
        self.tableWidgetKiralama()

    def yeni(self):
        self.ui.kiralama_aracId_text.setText('')
        self.ui.kiralama_musteriId_text.setText('')
        self.ui.kiralama_baslangic_text.setText('')
        self.ui.kiralama_bitis_text.setText('')
        self.ui.kiralama_kiraDurumu_text.setText('')


    def sil(self):

        response = QMessageBox.question(self, "Silme Onay", "Seçili kaydı silmek istediğinize emin misiniz?",
                                        QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:

            kira_id = self.ui.tableWidget_Kiralama.item(self.curRowIndex,0).text()  # kira id

            # Veritabanından kaydı sil
            self.cur.execute("DELETE FROM KIRA WHERE KIRA_ID= ?", (kira_id,))
            self.conn.commit()
            self.tableWidgetKiralama()
            QMessageBox.information(self, "Bilgilendirme", "Kaydınız Başarıyla Silinmiştir")

    def duzenle(self):
        musteri_id = self.ui.kiralama_musteriId_text.text()
        arac_id = self.ui.kiralama_aracId_text.text()
        baslangic = self.ui.kiralama_baslangic_text.text()
        bitis = self.ui.kiralama_bitis_text.text()
        durum = self.ui.kiralama_kiraDurumu_text.text()


        selected_row_index = self.ui.tableWidget_Kiralama.currentRow()

        # kira id
        kira_id_item = self.ui.tableWidget_Kiralama.item(selected_row_index, 0)


        kira_id = kira_id_item.text()

        # Kira verilerini güncelle
        self.cur.execute(
                "UPDATE KIRA SET MUSTERI_ID = ?, ARAC_ID = ?, KIRA_BASLA = ?, KIRA_BITIS = ? WHERE KIRA_ID = ?",
                (musteri_id, arac_id, baslangic, bitis, kira_id))
        self.cur.execute('UPDATE ARACLAR SET ARAC_DURUM = ? WHERE ARAC_ID = ?', [durum, arac_id])
        self.conn.commit()

        # tablo güncelleme
        self.tableWidgetKiralama()
        self.tableWidgetGosterArac()
        QMessageBox.information(self,'Bilgilendirme','Kayitlar Düzenlenmiştir')

    def cikis(self):
        kiralama.close()



if __name__ == "__main__":
    app = QApplication([])
    kiralama = Kiralama()
    kiralama.show()
    sys.exit(app.exec_())