# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aracEklemeMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(696, 597)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 661, 311))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 631, 192))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.araclar_sol_ilerle = QtWidgets.QToolButton(self.groupBox)
        self.araclar_sol_ilerle.setGeometry(QtCore.QRect(20, 250, 25, 19))
        self.araclar_sol_ilerle.setArrowType(QtCore.Qt.LeftArrow)
        self.araclar_sol_ilerle.setObjectName("araclar_sol_ilerle")
        self.araclar_sag_ilerle = QtWidgets.QToolButton(self.groupBox)
        self.araclar_sag_ilerle.setGeometry(QtCore.QRect(50, 250, 25, 19))
        self.araclar_sag_ilerle.setArrowType(QtCore.Qt.RightArrow)
        self.araclar_sag_ilerle.setObjectName("araclar_sag_ilerle")
        self.araclarComboBox = QtWidgets.QComboBox(self.groupBox)
        self.araclarComboBox.setGeometry(QtCore.QRect(460, 20, 91, 22))
        self.araclarComboBox.setObjectName("araclarComboBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(140, 250, 61, 20))
        self.label_5.setObjectName("label_5")
        self.kayitsayisiLabel = QtWidgets.QLabel(self.groupBox)
        self.kayitsayisiLabel.setGeometry(QtCore.QRect(210, 254, 47, 13))
        self.kayitsayisiLabel.setObjectName("kayitsayisiLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 340, 391, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 51, 16))
        self.label_4.setObjectName("label_4")
        self.ekleme_plaka_text = QtWidgets.QLineEdit(self.groupBox_2)
        self.ekleme_plaka_text.setGeometry(QtCore.QRect(120, 40, 141, 20))
        self.ekleme_plaka_text.setObjectName("ekleme_plaka_text")
        self.ekleme_marka_text = QtWidgets.QLineEdit(self.groupBox_2)
        self.ekleme_marka_text.setGeometry(QtCore.QRect(120, 60, 141, 20))
        self.ekleme_marka_text.setObjectName("ekleme_marka_text")
        self.ekleme_model_text = QtWidgets.QLineEdit(self.groupBox_2)
        self.ekleme_model_text.setGeometry(QtCore.QRect(120, 80, 141, 20))
        self.ekleme_model_text.setObjectName("ekleme_model_text")
        self.ekleme_yil_text = QtWidgets.QLineEdit(self.groupBox_2)
        self.ekleme_yil_text.setGeometry(QtCore.QRect(120, 100, 141, 20))
        self.ekleme_yil_text.setObjectName("ekleme_yil_text")
        self.ekleme_button_YENI = QtWidgets.QPushButton(self.groupBox_2)
        self.ekleme_button_YENI.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.ekleme_button_YENI.setObjectName("ekleme_button_YENI")
        self.ekleme_button_EKLE = QtWidgets.QPushButton(self.groupBox_2)
        self.ekleme_button_EKLE.setGeometry(QtCore.QRect(290, 70, 75, 23))
        self.ekleme_button_EKLE.setObjectName("ekleme_button_EKLE")
        self.ekleme_button_Duzenle = QtWidgets.QPushButton(self.groupBox_2)
        self.ekleme_button_Duzenle.setGeometry(QtCore.QRect(290, 100, 75, 23))
        self.ekleme_button_Duzenle.setObjectName("ekleme_button_Duzenle")
        self.ekleme_button_sil = QtWidgets.QPushButton(self.groupBox_2)
        self.ekleme_button_sil.setGeometry(QtCore.QRect(290, 130, 75, 23))
        self.ekleme_button_sil.setObjectName("ekleme_button_sil")
        self.ekleme_button_cikis = QtWidgets.QPushButton(self.groupBox_2)
        self.ekleme_button_cikis.setGeometry(QtCore.QRect(290, 160, 75, 23))
        self.ekleme_button_cikis.setObjectName("ekleme_button_cikis")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(190, 550, 321, 21))
        self.label_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Arac Ekleme"))
        self.groupBox.setTitle(_translate("Dialog", "Araçlar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Arac Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Arac Plaka"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Arac Marka"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Arac Model"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Arac Yıl"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Arac Durum"))
        self.araclar_sol_ilerle.setText(_translate("Dialog", "..."))
        self.araclar_sag_ilerle.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "Kayıt Sayısı : "))
        self.kayitsayisiLabel.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_2.setTitle(_translate("Dialog", "Ekleme Menu"))
        self.label.setText(_translate("Dialog", "Arac Plakasi"))
        self.label_2.setText(_translate("Dialog", "Arac Markası"))
        self.label_3.setText(_translate("Dialog", "Arac Modeli"))
        self.label_4.setText(_translate("Dialog", "Arac Yılı"))
        self.ekleme_button_YENI.setText(_translate("Dialog", "Yeni"))
        self.ekleme_button_EKLE.setText(_translate("Dialog", "Ekle"))
        self.ekleme_button_Duzenle.setText(_translate("Dialog", "Düzenle"))
        self.ekleme_button_sil.setText(_translate("Dialog", "Sil"))
        self.ekleme_button_cikis.setText(_translate("Dialog", "Çıkış"))
        self.label_7.setText(_translate("Dialog", "SEVINC RENT A CAR SYSTEM"))
