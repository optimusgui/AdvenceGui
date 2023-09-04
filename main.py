import random
import sys
import snap7
from snap7.types import *
from snap7.util import *
import stylesheet_variables as style_vars
import sqlite3
from datetime import datetime
import requests
import json
from printer_fonksiyonlar import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from GUI_PY.ui_MainWindow import Ui_MainWindow
from GUI_PY.ui_SplashWindow import *
from GUI_PY.ui_Ayarlar import *
from GUI_PY.ui_Ayarlar_kamera import *
from GUI_PY.ui_PLC import *

import pyodbc
import pymssql
import pypyodbc

from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QLabel, QPushButton, QVBoxLayout, QMessageBox

import time
import os
from openpyxl import load_workbook, Workbook
import threading

from zeep import Client, helpers
from zeep.transports import Transport
from requests import Session as WebServiceSession
from requests.auth import HTTPBasicAuth


from collections import defaultdict
from random import randint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QStackedWidget


# TODO Main
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.anapencere = Ui_MainWindow()
        self.anapencere.setupUi(self)
        self.anapencere.stackedWidgetMenuler.setCurrentWidget(self.anapencere.pageMain)

        self.anapencere.pushButtonClose.clicked.connect(lambda: self.close())
        self.anapencere.pushButtonSwitchTopageMain.clicked.connect(self.switchToOtherMainPage)
        self.anapencere.pushButtonSwitchTopageDatabase.clicked.connect(self.switchToOtherMainPage)
        self.anapencere.pushButtonOpenLoginMenu.clicked.connect(self.loginMenuOpenClose)
        self.anapencere.pushButtonOpenOperatorMenu.clicked.connect(self.operatorLoginMenuOpenClose)

        self.anapencere.pushButtonSwitchTopageLog.clicked.connect(self.switchToOtherMainPage)
        self.anapencere.pushButtonSwitchTopageSettings.clicked.connect(self.switchToOtherMainPage)

        self.anapencere.pushButtonButtonMenuToggle.clicked.connect(self.buton_menu_toggle)
        self.anapencere.widgetSagAcilirMenu.setVisible(False)
        self.anapencere.pushButtonSagAcilirMenuKapat.clicked.connect(self.widgetSagAcilirMenuKapatButon)
        self.anapencere.pushButtonLogFiltreEnable.clicked.connect(self.isLogFilterVisible)
        self.anapencere.pushButtonGirisYap.clicked.connect(self.girisYapButon)
        self.anapencere.pushButtonCikisYap.clicked.connect(self.cikisYapButon)
        self.anapencere.pushButtonOperatorGirisYap.clicked.connect(self.operatorGiris)
        self.anapencere.pushButtonOperatorCikisYap.clicked.connect(self.operatorCikis)
        self.anapencere.pushButtonAyarlarDetay.clicked.connect(self.Ayarlar)

        self.yeni_log_durumu = False

        # EMPTY
        self.RadioButtonTimer = QtCore.QTimer()
        self.RadioButtonTimer.timeout.connect(self.statusShow)
        self.RadioButtonTimer.setInterval(50)
        self.statusVariable = 0
        self.RadioButtonTimer.start()

        self.anapencere.pageSettings.setEnabled(True) #KAPAT

        QtCore.QTimer.singleShot(100, lambda: self.baslangic_fonksiyonlarini_cagir())


    def baslangic_fonksiyonlarini_cagir(self):
        pass

        #self.baglantiAyarlariniYukle()
        #self.PLCStrecConnect()
        #self.PLCRobotConnect()
        #self.mssql_baglanti()

    # TODO PLC HABERLEŞME
    """def PLCStrecConnect(self):
        try:
            if self.PLCStrecReadTimer.isActive():
                self.PLCStrecReadTimer.stop()

            if self.PLC_Strec.get_connected():
                self.PLC_Strec.destroy()
                self.PLC_Strec = snap7.client.Client()

            self.PLC_Strec.connect(self.PLC_STREC_IP, 0, 0)
            self.PLCConnectionStatusSTREC = self.PLC_Strec.get_connected()
            if self.PLCConnectionStatusSTREC:  # arayuzden adına bakılacak
                self.anapencere.labelPlcConnectionStatusStrec.setStyleSheet(style_vars.stylesheet_green)
                self.anapencere.labelPlcConnectionStatusStrec.setText("ONLINE")
                if not self.PLCStrecReadTimer.isActive():
                    self.PLCStrecReadTimer.start()
                    pass
                if self.PLCReconnectionTimerSTREC.isActive():
                    self.PLCReconnectionTimerSTREC.stop()
            else:
                self.anapencere.labelPlcConnectionStatusStrec.setStyleSheet(style_vars.stylesheet_red)
                self.anapencere.labelPlcConnectionStatusStrec.setText("OFFLINE")
                time.sleep(0.1)
                pass
            return self.PLCConnectionStatusSTREC

        except Exception as e:
            self.anapencere.labelPlcConnectionStatusStrec.setStyleSheet(style_vars.stylesheet_red)
            self.anapencere.labelPlcConnectionStatusStrec.setText("OFFLINE")
            self.log_yaz("PLC BAGLANTI HATASI", str(e))
            if not self.PLCReconnectionTimerSTREC.isActive():
                self.PLCReconnectionTimerSTREC.start()
            return False
            pass"""

    # TODO PLC DATABLOK HABERLEŞME
    """def PLCStrecOkumaYazmaDongu(self):
        try:
            dongu_start = time.time()
            if self.PLCConnectionStatusSTREC:
                plc_sinyal_area_data = self.PLC_Strec.read_area(snap7.types.Areas.DB, self.PLC_STREC_DB, 0, 32)

                self.PLCStrecSinyalleriGoster(plc_sinyal_area_data)  # butonlar olarak değişecek
                if not get_bool(plc_sinyal_area_data, 0, 0):  # Benden giden pc ye surekli
                    set_bool(plc_sinyal_area_data, 0, 0, True)

                PLC_GELEN_SINYAL_LIST = [
                    get_bool(plc_sinyal_area_data, 6, 1),  # Hat 1 Etiket Bas 1
                    get_bool(plc_sinyal_area_data, 6, 2)  # Hat 1 PLC Etiket Bastım Sinyali Yapıstırdım
                ]

                if PLC_GELEN_SINYAL_LIST[0] != self.PLC_STREC_GELEN_SINYAL_LIST_OLD[0]:
                    if PLC_GELEN_SINYAL_LIST[0]:
                        self.STREC_Etiket_Bas()

                if PLC_GELEN_SINYAL_LIST[1] != self.PLC_STREC_GELEN_SINYAL_LIST_OLD[1]:
                    if PLC_GELEN_SINYAL_LIST[1]:
                        self.STREC_PLC_Etiket_Kontrol()

                if self.PLC_GIDEN_SINYAL_YAZICI_STREC_ETIKET_CIKTI:
                    if not get_bool(plc_sinyal_area_data, 0, 1):
                        set_bool(plc_sinyal_area_data, 0, 1, True)
                    else:
                        self.PLC_GIDEN_SINYAL_YAZICI_STREC_ETIKET_CIKTI = False

                if self.PLC_GIDEN_SINYAL_YAZICI_STREC_ETIKET_OLUSTURMA_HATADA:
                    if not get_bool(plc_sinyal_area_data, 0, 3):
                        set_bool(plc_sinyal_area_data, 0, 3, True)
                    else:
                        self.PLC_GIDEN_SINYAL_YAZICI_STREC_ETIKET_OLUSTURMA_HATADA = False

                if self.PLC_GIDEN_SINYAL_STREC_ETIKET_DURUMU:
                    set_bool(plc_sinyal_area_data, 6, 2, False)
                else:
                    set_bool(plc_sinyal_area_data, 6, 2, False)

                # YAZICI HATADA SINYALLERI PLC 1
                if self.PLC_GIDEN_SINYAL_YAZICI_STREC_YAZICI_HATADA:
                    if not get_bool(plc_sinyal_area_data, 0, 2):
                        set_bool(plc_sinyal_area_data, 0, 2, True)
                    else:
                        self.PLC_GIDEN_SINYAL_YAZICI_STREC_YAZICI_HATADA = False

                # ESLESME DONUSLERI
                if self.PALET_ETIKET_ESLESME_BASARALI:
                    if not get_bool(plc_sinyal_area_data, 0, 4):
                        set_bool(plc_sinyal_area_data, 0, 4, True)
                    else:
                        self.PALET_ETIKET_ESLESME_BASARALI = False

                if self.PALET_ETIKET_ESLESME_BASARISIZ:
                    if not get_bool(plc_sinyal_area_data, 0, 5):
                        set_bool(plc_sinyal_area_data, 0, 5, True)
                    else:
                        self.PALET_ETIKET_ESLESME_BASARISIZ = False

                self.PLC_STREC_GELEN_SINYAL_LIST_OLD = PLC_GELEN_SINYAL_LIST
                self.PLC_Strec.db_write(self.PLC_STREC_DB, 0, plc_sinyal_area_data)

            dongu_stop = time.time()
            dongu_tepki_suresi = (dongu_stop - dongu_start) * 1000
            self.anapencere.labelPlcCycleTimeStrec.setText("{:.2f} ms".format(dongu_tepki_suresi))
        except Exception as e:
            self.anapencere.labelPlcConnectionStatusStrec.setStyleSheet(style_vars.stylesheet_red)
            self.anapencere.labelPlcConnectionStatusStrec.setText("OFFLINE")
            self.log_yaz("STREC PLC OKUMA HATASI", str(e))
            if not self.PLCReconnectionTimerSTREC.isActive():
                self.PLCReconnectionTimerSTREC.start()
            pass"""

    # TODO PLC SİNYALLERI GOSTER
    """def PLCStrecSinyalleriGoster(self, plc_sinyal_data):
        try:
            time_start = time.time()
            self.anapencere.pushButtonPCHaberlesmeStrec.setChecked(get_bool(plc_sinyal_data, 0, 0))
            self.anapencere.pushButtonPLCHaberlesmeStrec.setChecked(get_bool(plc_sinyal_data, 6, 0))

            # GELEN VERILER
            self.anapencere.labelStrec_Palet_Numarasi.setText(str(get_dint(plc_sinyal_data, 8)))
            self.anapencere.labelStrec_Recete_Bilgisi.setText(str(get_int(plc_sinyal_data, 12)))
            self.anapencere.labelStrec_Adet_Bilgisi.setText(str(get_int(plc_sinyal_data, 14)))
            self.anapencere.labelStrec_Dara_Agirlik.setText(str(get_real(plc_sinyal_data, 16)))
            self.anapencere.labelStrec_Net_Agirlik.setText(str(get_real(plc_sinyal_data, 20)))
            self.anapencere.labelStrec_Brut_Agirlik.setText(str(get_real(plc_sinyal_data, 24)))
            self.anapencere.labelStrec_Toplam_Agirlik.setText(str(get_real(plc_sinyal_data, 28)))

            # STREC ICIN SINYALLER GELEN
            self.anapencere.pushButtonStrec_Etiket_Bas.setChecked(get_bool(plc_sinyal_data, 6, 1))
            self.anapencere.pushButtonStrec_Etiket_Durumu.setChecked(get_bool(plc_sinyal_data, 6, 2))

            # STREC GIDEN SINYALLER PLC YE
            self.anapencere.pushButtonStrec_Etiket_Bastim.setChecked(get_bool(plc_sinyal_data, 0, 1))
            self.anapencere.pushButtonStrec_Yazici_Hatada.setChecked(get_bool(plc_sinyal_data, 0, 2))
            self.anapencere.pushButtonStrec_Etiket_Olusturma_Hatada.setChecked(get_bool(plc_sinyal_data, 0, 3))
            self.anapencere.pushButtonStrec_Eslesme_Basarili.setChecked(get_bool(plc_sinyal_data, 0, 4))
            self.anapencere.pushButtonStrec_Eslesme_Basarisiz.setChecked(get_bool(plc_sinyal_data, 0, 5))

            # palet_num
            time_stop = time.time()

            dongu_suresi = (time_stop - time_start) * 1000
            self.anapencere.labelPlcSinyalGosterDonguSuresiStrec.setText("{:.2f} ms".format(dongu_suresi))
            pass
        except Exception as e:
            self.log_yaz("PLC STREC SINYALLERI GOSTERME HATASI", str(e))
            pass"""

    # TODO MSSQL BAGLANTI
    """def mssql_baglanti(self):
        try:
            if not self.LOKAL_DATABASE_CONNECTION_STATUS:
                self.local_db = pymssql.connect(server=self.DB_SERVER,
                                                database=self.DB_VERITABANI,
                                                user=self.DB_USERNAME,
                                                password=self.DB_PASSWORD)
                self.database_cursor = self.local_db.cursor()

                self.LOKAL_DATABASE_CONNECTION_STATUS = True
                self.anapencere.labelDatabaseConnectionStatus.setStyleSheet(style_vars.stylesheet_green)
                self.anapencere.labelDatabaseConnectionStatus.setText("ONLINE")
        except Exception as e:
            self.LOKAL_DATABASE_CONNECTION_STATUS = False
            self.anapencere.labelDatabaseConnectionStatus.setStyleSheet(style_vars.stylesheet_red)
            self.anapencere.labelDatabaseConnectionStatus.setText("OFFLINE")
            self.log_yaz("DATABASE", str(e))"""

    def Ayarlar(self):
        self.ayarlar = Ayarlar()
        self.ayarlar.show()
        
    def girisYapButon(self):
        kullanici_adi = self.anapencere.lineEditKullanici.text()
        kullanici_sifre = self.anapencere.lineEditSifre.text()

        if kullanici_adi == 'stu' and kullanici_sifre == 'optimak123':
            self.anapencere.pageSettings.setEnabled(True)
            # self.anapencere.widgetManuelSinyalActivate.setVisible(True)
        else:
            self.anapencere.pageSettings.setEnabled(False)
            # self.anapencere.pushButtonTestModeIsActive.setVisible(False)

    def cikisYapButon(self):
        self.anapencere.pageSettings.setEnabled(False)
        # self.anapencere.widgetManuelSinyalActivate.setEnabled(True)

    def operatorGiris(self):
        try:
            operator_adi = self.anapencere.comboBoxOperatorKullaniciAdi.currentText()
            operator_sifre = self.anapencere.lineEditOperatorSifre.text()

            with sqlite3.connect("datalar/operatorlerDatabase.db", isolation_level=None) as connector:

                connector.row_factory = sqlite3.Row
                sqlite_cursor = connector.cursor()
                sqlite_cursor.execute(f"SELECT Count(*) FROM OperatorBilgileri where OperatorKullaniciAdi = '{operator_adi}' and OperatorSifre = '{operator_sifre}'")
                gelen_data = sqlite_cursor.fetchone()
                if gelen_data[0] == 1:
                    self.anapencere.labelOperatorAdi.setText(operator_adi)
                else:
                    self.log_yaz("KULLANICI ADI VE SİFREYİ KONTROL EDİNİZ!!!", "")
        except Exception as e:
            self.log_yaz("OPERATOR GIRIS ISLEMI BASARISIZ", str(e))

    def operatorCikis(self):
        try:
            self.anapencere.labelOperatorAdi.setText("GİRİŞ YAPINIZ!!!")
            self.anapencere.lineEditOperatorSifre.clear()
        except Exception as e:
            self.log_yaz("OPERATOR CIKIS ISLEMI BASARISIZ", str(e))

    # TODO BAGLANTI AYARLARI YUKLEME
    """def baglantiAyarlariniYukle(self):
        try:
            with sqlite3.connect("datalar/portsDatabase.db", isolation_level=None) as connector:

                connector.row_factory = sqlite3.Row
                sqlite_cursor = connector.cursor()
                sqlite_cursor.execute("SELECT * FROM connection_port WHERE ref='{}';".format(1))
                temporary_data = sqlite_cursor.fetchone()

                self.PLC_ROBOT_IP = temporary_data["PLC_IP_ROBOT"]
                self.anapencere.lineEditAyarlarPlcRobotIp.setText(str(self.PLC_ROBOT_IP))
                self.PLC_ROBOT_BOBIN_DB = temporary_data["PLC_DB_ROBOT_1"]  #bobin
                self.anapencere.spinBoxAyarlarHaberlesmeRobotDbNum_1.setValue(int(self.PLC_ROBOT_BOBIN_DB))
                self.PLC_ROBOT_KOLI_DB = temporary_data["PLC_DB_ROBOT_2"] #koli
                self.anapencere.spinBoxAyarlarHaberlesmeRobotDbNum_2.setValue(int(self.PLC_ROBOT_KOLI_DB))

                self.PLC_STREC_IP = temporary_data["PLC_IP_STREC"]
                self.anapencere.lineEditAyarlarPlcStrecIp.setText(str(self.PLC_STREC_IP))
                self.PLC_STREC_DB = temporary_data["PLC_DB_STREC"]
                self.anapencere.spinBoxAyarlarHaberlesmeStrecDbNum_1.setValue(int(self.PLC_STREC_DB))

                self.DB_USERNAME = temporary_data["DB_USERNAME"]
                self.anapencere.lineEditAyarlarUsername.setText(str(self.DB_USERNAME))
                self.DB_PASSWORD = temporary_data["DB_PASSWORD"]
                self.anapencere.lineEditAyarlarPassword.setText(str(self.DB_PASSWORD))
                self.DB_VERITABANI = temporary_data["DB_VERITABANI"]
                self.anapencere.lineEditAyarlarVeritabani.setText(str(self.DB_VERITABANI))
                self.DB_SERVER = temporary_data["DB_SERVER"]
                self.anapencere.lineEditAyarlarServer.setText(str(self.DB_SERVER))

                self.PLC_YAZICI_ADI_1 = temporary_data["YAZICI_ADI_1"]
                self.anapencere.lineEditAyarlarYazici_1.setText(str(self.PLC_YAZICI_ADI_1))
                self.PLC_YAZICI_ADI_2 = temporary_data["YAZICI_ADI_2"]
                self.anapencere.lineEditAyarlarYazici_2.setText(str(self.PLC_YAZICI_ADI_2))
                self.PLC_YAZICI_ADI_3 = temporary_data["YAZICI_ADI_3"]
                self.anapencere.lineEditAyarlarYazici_3.setText(str(self.PLC_YAZICI_ADI_3))

                connector.row_factory = sqlite3.Row
                sqlite_cursor_2 = connector.cursor()
                sqlite_cursor_2.execute("SELECT * FROM connection_port_2 WHERE ref='{}';".format(1))
                temporary_data_2 = sqlite_cursor_2.fetchone()

                self.VARDIYA_1 = temporary_data_2["var1_CheckBox"]
                if self.VARDIYA_1 == 1:
                    self.anapencere.checkBoxVardiya_1.setChecked(True)
                else:
                    self.anapencere.checkBoxVardiya_1.setChecked(False)

                self.VARDIYA_2 = temporary_data_2["var2_CheckBox"]
                if self.VARDIYA_2 == 1:
                    self.anapencere.checkBoxVardiya_2.setChecked(True)
                else:
                    self.anapencere.checkBoxVardiya_2.setChecked(False)

                self.VARDIYA_3 = temporary_data_2["var3_CheckBox"]
                if self.VARDIYA_3 == 1:
                    self.anapencere.checkBoxVardiya_3.setChecked(True)
                else:
                    self.anapencere.checkBoxVardiya_3.setChecked(False)

        except Exception as e:
            self.log_yaz("BAGLANTI AYARLARINI YUKLEME HATASI", str(e))
            pass"""

    # TODO YAZICI AYARLARI YUKLEME
    """def yazicilarDurumKontrol(self, RobotBobinStatus, RobotBobinStatusStr, RobotKoliStatus, RobotKoliStatusStr, paletlemeYaziciStatus, paletlemeYaziciStr):

        self.bobinAyirmaBuyukYaziciStatus = RobotKoliStatus
        self.bobinAyirmaKucukYaziciStatus = RobotBobinStatus
        self.paletlemeYaziciStatus = paletlemeYaziciStatus

        self.anapencere.labelRobotBobinStatus.setText(f"BOBIN : {RobotBobinStatusStr}")
        self.anapencere.labelRobotKoliStatus.setText(f"KOLI : {RobotKoliStatusStr}")
        self.anapencere.labelPaletStatus.setText(f"PALET : {paletlemeYaziciStr}")


        if RobotKoliStatus == 1024 or RobotKoliStatus == 0:
            self.PLC_GIDEN_SINYAL_YAZICI_ROBOT_KOLI_YAZICI_HATADA = False
            if RobotKoliStatus == 1024:
                self.anapencere.labelRobotKoliStatus.setStyleSheet(style_vars.stylesheet_yellow)
            else:
                self.anapencere.labelRobotKoliStatus.setStyleSheet(style_vars.stylesheet_green)
        else:
            self.PLC_GIDEN_SINYAL_YAZICI_ROBOT_KOLI_YAZICI_HATADA = True
            self.anapencere.labelRobotKoliStatus.setStyleSheet(style_vars.stylesheet_red)

        if RobotBobinStatus == 1024 or RobotBobinStatus == 0:
            self.PLC_GIDEN_SINYAL_YAZICI_ROBOT_BOBIN_YAZICI_HATADA = False
            if RobotBobinStatus == 1024:
                self.anapencere.labelRobotBobinStatus.setStyleSheet(style_vars.stylesheet_yellow)
            else:
                self.anapencere.labelRobotBobinStatus.setStyleSheet(style_vars.stylesheet_green)
        else:
            self.PLC_GIDEN_SINYAL_YAZICI_ROBOT_BOBIN_YAZICI_HATADA = True
            self.anapencere.labelRobotBobinStatus.setStyleSheet(style_vars.stylesheet_red)

        if paletlemeYaziciStatus == 1024 or paletlemeYaziciStatus == 0:
            self.PLC_GIDEN_SINYAL_YAZICI_STREC_YAZICI_HATADA = False
            if paletlemeYaziciStatus == 1024:
                self.anapencere.labelPaletStatus.setStyleSheet(style_vars.stylesheet_yellow)
            else:
                self.anapencere.labelPaletStatus.setStyleSheet(style_vars.stylesheet_green)
        else:
            self.PLC_GIDEN_SINYAL_YAZICI_STREC_YAZICI_HATADA = True
            self.anapencere.labelPaletStatus.setStyleSheet(style_vars.stylesheet_red)
"""

    # TODO AYARLARI KAYDET
    """def ayarlariKaydet(self):
        try:
            with sqlite3.connect("datalar/portsDatabase.db", isolation_level=None) as connector:
                connector.row_factory = sqlite3.Row
                sqlite_cursor = connector.cursor()

                plc_Ip_Robot = self.anapencere.lineEditAyarlarPlcRobotIp.text().replace(" ", "").replace(
                    ",", ".")
                plc_DbNum_Robot_1 = self.anapencere.spinBoxAyarlarHaberlesmeRobotDbNum_1.value()
                plc_DbNum_Robot_2 = self.anapencere.spinBoxAyarlarHaberlesmeRobotDbNum_2.value()

                plc_Ip_Strec = self.anapencere.lineEditAyarlarPlcStrecIp.text().replace(" ", "").replace(
                    ",", ".")
                plc_DbNum_Strec = self.anapencere.spinBoxAyarlarHaberlesmeStrecDbNum_1.value()

                db_server = self.anapencere.lineEditAyarlarServer.text()
                db_veritabani = self.anapencere.lineEditAyarlarVeritabani.text()
                db_username = self.anapencere.lineEditAyarlarUsername.text()
                db_password = self.anapencere.lineEditAyarlarPassword.text()

                yazici_adi_1 = self.anapencere.lineEditAyarlarYazici_1.text()
                yazici_adi_2 = self.anapencere.lineEditAyarlarYazici_2.text()
                yazici_adi_3 = self.anapencere.lineEditAyarlarYazici_3.text()

                sqlite_cursor.execute(
                    "UPDATE connection_port SET PLC_IP_ROBOT = '{}', PLC_DB_ROBOT_1 = '{}',PLC_DB_ROBOT_2 = '{}',PLC_IP_STREC = '{}', PLC_DB_STREC = '{}', DB_USERNAME = '{}', DB_PASSWORD = '{}', DB_VERITABANI = '{}', DB_SERVER = '{}', YAZICI_ADI_1 = '{}', YAZICI_ADI_2 = '{}', YAZICI_ADI_3 = '{}' WHERE ref= '{}';".format(
                        plc_Ip_Robot, plc_DbNum_Robot_1, plc_DbNum_Robot_2, plc_Ip_Strec, plc_DbNum_Strec, db_username, db_password, db_veritabani, db_server, yazici_adi_1, yazici_adi_2, yazici_adi_3, 1))

                if sqlite_cursor.rowcount < 1:
                    self.anapencere.labelAyarlarLog.setText(
                        "AYARLAR KAYDEDILEMEDI.\n LÜTFEN GİRDİĞİNİZ DEĞERLERİ KOTROL EDİNİZ.")

                else:
                    self.anapencere.labelAyarlarLog.setText("AYARLAR KAYDEDILDI")
                    self.PLC_ROBOT_IP = plc_Ip_Robot
                    self.PLC_ROBOT_BOBIN_DB = plc_DbNum_Robot_1
                    self.PLC_ROBOT_KOLI_DB = plc_DbNum_Robot_2

                    self.PLC_STREC_IP = plc_Ip_Strec
                    self.PLC_STREC_DB = plc_DbNum_Strec
                    self.DB_SERVER = db_server
                    self.DB_VERITABANI = db_veritabani
                    self.DB_USERNAME = db_username
                    self.DB_PASSWORD = db_password

                    self.PLC_YAZICI_ADI_1 = yazici_adi_1
                    self.PLC_YAZICI_ADI_2 = yazici_adi_2
                    self.PLC_YAZICI_ADI_3 = yazici_adi_3


                    self.yazicilariKontrolThread.ayar_transfer(yazici_adi_1, yazici_adi_2, yazici_adi_3)

        except Exception as e:
            self.log_yaz("AYAR KAYDETME HATASI:", str(e))
            pass"""

    def loginMenuOpenClose(self):
        try:
            if self.sender().isChecked():
                self.anapencere.stackedWidgetSagAcilirMenu.setCurrentWidget(self.anapencere.pageGirisCikisYap)
                self.anapencere.widgetSagAcilirMenu.setVisible(True)
                self.anapencere.widgetSagAcilirMenu.setMaximumSize(QtCore.QSize(250, 16777215))

                self.palet_detay_goster_sender = None
                self.sender().setStyleSheet(style_vars.buttons_menu_active)
            else:
                self.anapencere.widgetSagAcilirMenu.setVisible(False)
                self.sender().setStyleSheet(style_vars.buttons_menu_normal)
        except Exception as e:
            self.log_yaz("loginMenuOpenClose", "")
            pass
    def operatorLoginMenuOpenClose(self):
        try:
            self.anapencere.comboBoxOperatorKullaniciAdi.clear()
            if self.sender().isChecked():
                self.anapencere.stackedWidgetSagAcilirMenu.setCurrentWidget(self.anapencere.pageOperatorGirisCikisYap)
                self.anapencere.widgetSagAcilirMenu.setVisible(True)
                self.anapencere.widgetSagAcilirMenu.setMaximumSize(QtCore.QSize(250, 16777215))

                self.palet_detay_goster_sender = None
                self.sender().setStyleSheet(style_vars.buttons_menu_active)

                with sqlite3.connect("datalar/operatorlerDatabase.db", isolation_level=None) as connector:

                    connector.row_factory = sqlite3.Row
                    sqlite_cursor = connector.cursor()
                    sqlite_cursor.execute("SELECT OperatorKullaniciAdi FROM OperatorBilgileri")
                    kullanici_adlari = sqlite_cursor.fetchall()
                    for kullanici_adı in kullanici_adlari:
                        self.anapencere.comboBoxOperatorKullaniciAdi.addItem(kullanici_adı[0])
            else:
                self.anapencere.widgetSagAcilirMenu.setVisible(False)
                self.sender().setStyleSheet(style_vars.buttons_menu_normal)
        except Exception as e:
            self.log_yaz("operatorLoginMenuOpenClose", str(e))
            pass

    def filtreleriTemizle(self):
        self.anapencere.lineEditLogFiltreTarih.setText("")
        self.anapencere.lineEditLogFiltreKaynak.setText("")
        self.anapencere.lineEditLogFiltreHata.setText("")

    def buton_menu_toggle(self):
        if self.sender().text() == "":
            buton_liste = self.sender().parentWidget().findChildren(QtWidgets.QPushButton)
            for butonn in buton_liste:
                butonn.setText(butonn.toolTip().ljust(15, " "))
                butonn.setMinimumSize(QtCore.QSize(145, 0))
            self.sender().parentWidget().setMinimumSize(QtCore.QSize(150, 0))

        elif self.sender().text() == self.sender().toolTip().ljust(15, " "):
            buton_liste = self.sender().parentWidget().findChildren(QtWidgets.QPushButton)
            for butonn in buton_liste:
                butonn.setMinimumSize(QtCore.QSize(40, 0))
                butonn.setText("")

            self.sender().parentWidget().setMinimumSize(QtCore.QSize(45, 0))

    def switchToOtherMainPage(self):
        # signal slot baglantısı Designer Uzerinden yapılmıstır

        # todo: aşağıdaki tablo yenilemelerinde kontrol ve hata verme sağlanacak
        pageName = self.sender().objectName().replace("pushButtonSwitchTo", "")
        self.clear_menu_button_styls(self.sender())

        switchPage = self.findChild(QtWidgets.QWidget, pageName)
        switchPage.parentWidget().setCurrentWidget(switchPage)
        self.sender().setStyleSheet(style_vars.buttons_menu_active)
        primaryPage = self.anapencere.stackedWidgetMenuler.currentWidget().objectName()

        if primaryPage == "pageLog":
            QtCore.QTimer.singleShot(100, lambda: self.loadLogDatabase())
            self.yeni_log_durumu = False

    def clear_menu_button_styls(self, sender):
        try:
            buton_liste = sender.parentWidget().findChildren(QtWidgets.QPushButton)
            for butonn in buton_liste:
                if butonn.objectName() == "pushButtonSwitchTopageLog":
                    if not self.yeni_log_durumu:
                        butonn.setStyleSheet(style_vars.buttons_menu_normal)
                elif butonn.objectName() == "pushButtonOpenLoginMenu":
                    continue
                elif butonn.objectName() == "pushButtonOpenOperatorMenu":
                    continue
                elif butonn.objectName() == "pushButtonClose":
                    continue
                else:
                    butonn.setStyleSheet(style_vars.buttons_menu_normal)

        except Exception as e:
            print("clear menu button styls exception", e)
            pass

    def widgetSagAcilirMenuKapatButon(self):
        try:
            self.anapencere.widgetSagAcilirMenu.setVisible(False)
            self.palet_detay_goster_sender = None
            self.anapencere.pushButtonOpenLoginMenu.setChecked(False)
            self.anapencere.pushButtonOpenLoginMenu.setStyleSheet(style_vars.buttons_menu_normal)
        except:
            pass

    def statusShow(self):
        """if len(self.plc_istek_list) > 0:
            self.anapencere.listWidgetPlcIstekList.clear()
            for istek in self.plc_istek_list:
                item = QtWidgets.QListWidgetItem()
                item.setText(istek)
                self.anapencere.listWidgetPlcIstekList.addItem(item)
            son_satir = self.anapencere.listWidgetPlcIstekList.count()
            son_item = self.anapencere.listWidgetPlcIstekList.item(son_satir - 1)
            son_item.setBackground(QtGui.QColor('#7fc97f'))"""


        self.statusVariable += 5
        if self.statusVariable > 100:
            self.statusVariable = 0

        value = self.statusVariable

        progress = (100 - value) / 100.0

        stop_array = [None, None, None, None, None, None, None, None]

        stop_array[0] = progress
        stop_array[1] = progress + 0.002
        stop_array[2] = progress + 0.262
        stop_array[3] = progress + 0.264
        stop_array[4] = progress + 0.502
        stop_array[5] = progress + 0.504
        stop_array[6] = progress + 0.762
        stop_array[7] = progress + 0.764

        for i in range(0, 8):
            if stop_array[i] > 1:
                stop_array[i] = stop_array[i] - 1

        for i in range(0, 8):
            stop_array[i] = str(stop_array[i])
        mini_gosterge_styleSheet = style_vars.status_gosterge_styleSheet \
            .replace("{STOP_1_1}", stop_array[0]) \
            .replace("{STOP_1_2}", stop_array[1]) \
            .replace("{STOP_2_1}", stop_array[2]) \
            .replace("{STOP_2_2}", stop_array[3]) \
            .replace("{STOP_3_1}", stop_array[4]) \
            .replace("{STOP_3_2}", stop_array[5]) \
            .replace("{STOP_4_1}", stop_array[6]) \
            .replace("{STOP_4_2}", stop_array[7])

        self.anapencere.statusGostergeProgress.setStyleSheet(mini_gosterge_styleSheet)

    def loadLogDatabase(self):
        # todo: başka yere taşınacak
        try:
            with sqlite3.connect("datalar/logDatabase.db", isolation_level=None) as connector:
                self.isLogFilterVisible()
                connector.row_factory = sqlite3.Row
                sqlite_cursor = connector.cursor()
                sqlite_cursor.execute("SELECT * FROM log_kayitlari")

                tarih_filtre = self.anapencere.lineEditLogFiltreTarih.text()
                kaynak_filtre = self.anapencere.lineEditLogFiltreKaynak.text()
                log_yazisi_filtre = self.anapencere.lineEditLogFiltreHata.text()

                sqlite_cursor.execute(
                    """SELECT tarih, kaynak, log_yazisi FROM log_kayitlari WHERE tarih LIKE "%{tarih_filtre}%" AND 
                    kaynak LIKE "%{kaynak_filtre}%" AND log_yazisi LIKE "%{log_yazisi_filtre}%" ORDER BY 
                    ref;""".replace(
                        "{tarih_filtre}", tarih_filtre).
                        replace("{kaynak_filtre}", kaynak_filtre).replace("{log_yazisi_filtre}", log_yazisi_filtre))

                gelen_data = sqlite_cursor.fetchall()
                if len(gelen_data) != 0:
                    self.anapencere.widgetLogKaydiYokUyarisi.setVisible(False)
                    self.anapencere.tableWidgetLog.setVisible(True)
                    self.anapencere.tableWidgetLog.setSortingEnabled(False)
                    self.anapencere.tableWidgetLog.setRowCount(0)
                    for data in gelen_data:
                        rowPosition = self.anapencere.tableWidgetLog.rowCount()
                        self.anapencere.tableWidgetLog.insertRow(rowPosition)

                        item = QtWidgets.QTableWidgetItem(str(rowPosition + 1))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.anapencere.tableWidgetLog.setVerticalHeaderItem(rowPosition, item)

                        item = QtWidgets.QTableWidgetItem()
                        log_tarih = QDateTime.fromString(data["tarih"], "dd-MM-yyyy hh:mm:ss")
                        item.setData(Qt.DisplayRole, log_tarih)

                        self.anapencere.tableWidgetLog.setItem(rowPosition, 0, item)
                        self.anapencere.tableWidgetLog.setItem(rowPosition, 1,
                                                               QtWidgets.QTableWidgetItem(str(data["kaynak"])))
                        self.anapencere.tableWidgetLog.setItem(rowPosition, 2,
                                                               QtWidgets.QTableWidgetItem(str(data["log_yazisi"])))

                    self.anapencere.tableWidgetLog.resizeColumnsToContents()
                    self.anapencere.tableWidgetLog.setSortingEnabled(True)
                    self.anapencere.tableWidgetLog.sortByColumn(0, Qt.DescendingOrder)

                    maxwidth = self.anapencere.tableWidgetLog.verticalHeader().sectionSize(0)
                    self.anapencere.pushButtonLogFiltreEnable.setMinimumWidth(maxwidth)
                    self.anapencere.pushButtonLogFiltreEnable.setMaximumSize(maxwidth, 35)

                    maxwidth = self.anapencere.tableWidgetLog.horizontalHeader().sectionSize(0)
                    self.anapencere.lineEditLogFiltreTarih.setMinimumWidth(maxwidth)
                    self.anapencere.lineEditLogFiltreTarih.setMaximumSize(maxwidth, 30)

                    maxwidth = self.anapencere.tableWidgetLog.horizontalHeader().sectionSize(1)
                    self.anapencere.lineEditLogFiltreKaynak.setMinimumWidth(maxwidth)
                    self.anapencere.lineEditLogFiltreKaynak.setMaximumSize(maxwidth, 30)
                    # self.anapencere.widgetLogFiltreleri.layout().setContentsMargins(0, 0, 0, 0)
                else:
                    self.anapencere.tableWidgetLog.setVisible(False)
                    self.anapencere.widgetLogKaydiYokUyarisi.setVisible(True)
        except Exception as e:
            print(e)
            pass

    def isLogFilterVisible(self):
        self.anapencere.widgetLogFiltreleri.setVisible(self.anapencere.pushButtonLogFiltreEnable.isChecked())

    def log_yaz(self, kaynak, log_yazisi):
        try:
            self.yeni_log_durumu = True
            #self.anapencere.labelSayfaAltiLog.setText("{}: {}".format(kaynak, log_yazisi))
            self.anapencere.pushButtonSwitchTopageLog.setStyleSheet(style_vars.red_background)
            python_date = QDateTime.currentDateTime().toPyDateTime()
            datestring = python_date.strftime("%d-%m-%Y %H:%M:%S")
            log_yazisi = log_yazisi.replace('"', "'")

            with sqlite3.connect("datalar/logDatabase.db", isolation_level=None) as connector:
                connector.row_factory = sqlite3.Row
                sqlite_cursor = connector.cursor()
                sqlite_cursor.execute(
                    "CREATE TABLE IF NOT EXISTS log_kayitlari (ref INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,"
                    "tarih	TEXT,"
                    "kaynak TEXT,"
                    "log_yazisi	TEXT);")

                sqlite_cursor.execute(
                    "DELETE FROM {} where ref NOT IN( select ref from (select ref from {} order by ref desc LIMIT "
                    "{}) x); "
                    "".format("log_kayitlari", "log_kayitlari", 10000))

                command = """INSERT INTO log_kayitlari (tarih, kaynak, log_yazisi) VALUES ("{tarih}", "{kaynak}", 
                "{log_yazisi}");""".replace("{tarih}", datestring).replace("{kaynak}", str(kaynak)).replace(
                    "{log_yazisi}", log_yazisi)
                sqlite_cursor.execute(command)
        except Exception as e:
            print("log exception: ", e)
            pass

    def closeEvent(self, event):
        try:
            password_dialog = MyPasswordDialog()
            if password_dialog.exec_() == QDialog.Accepted:
                event.accept()
            else:
                event.ignore()
        except Exception as e:
            print("e", str(e))
            pass

class Ayarlar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ayarlar, self).__init__(parent=parent)
        
        self.ui = Ui_Ayarlar()
        self.ui.setupUi(self)
        self.ui.btn_Kamera.clicked.connect(self.Kamera_Ayarlar)
        self.ui.btn_PLC.clicked.connect(self.PLC_Ayarlar)
    
    def Kamera_Ayarlar(self):
        self.Kamera_Ayarlar = Kamera_Ayarlar()
        self.Kamera_Ayarlar.show()
    
    def PLC_Ayarlar(self):
        self.PLC_Ayarlar = PLC_Ayarlar()
        self.PLC_Ayarlar.show()

class Kamera_Ayarlar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Kamera_Ayarlar, self).__init__(parent=parent)
        
        self.ui = Ui_Ayarlar_Kamera()
        self.ui.setupUi(self)

class PLC_Ayarlar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(PLC_Ayarlar, self).__init__(parent=parent)
        
        self.ui = Ui_PLC()
        self.ui.setupUi(self)


class MyPasswordDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Şifre Etiketi ve Düzeni
        self.label = QLabel("PLEASE ENTER PASSWORD :")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_button = QPushButton("OK")
        self.password_button.clicked.connect(self.check_password)

        self.setStyleSheet("QWidget { background-color: #222; color: #fff; }")
        self.setWindowTitle("EXIT")

        # Düzenleme
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.password_button)
        self.setLayout(layout)

    def check_password(self):
        if self.password_edit.text() == "12345":
            self.accept()
        else:
            QMessageBox.warning(self, "Hata", "Yanlış Şifre")


class SplashScreen(QtWidgets.QMainWindow, Ui_SplashScreen):
    def __init__(self, parent=None):

        super(SplashScreen, self).__init__(parent=parent)

        self.splashpencere = Ui_SplashScreen()
        self.splashpencere.setupUi(self)

        self.splashpencere.pushButtonCancel.clicked.connect(self.buton_cancel)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.splashpencere.progressBar.setValue(0)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(255, 255, 255, 250))
        self.splashpencere.centralwidget.setGraphicsEffect(self.shadow)
        self.splashpencere.labelSoftwareVersion.setText("Version: 1.0 @2023")

        self.prograss_thread = SplashScreenThreadClass()
        self.prograss_thread.thread_kontrol_sinyal.connect(self.progress)
        self.thread_baslat()

    def buton_cancel(self):
        self.thread_durdur()
        self.close()

    def thread_baslat(self):
        self.prograss_thread.start()

    def thread_durdur(self):
        self.prograss_thread.terminate()

    def progress(self, ilerleme, durum):

        if ilerleme == 1:
            self.splashpencere.label_description.setText("BAGLANTILAR YUKLENIYOR")
        if ilerleme == 20:
            self.splashpencere.progressBar.setValue(ilerleme)
            if durum:
                self.splashpencere.listWidgetIslemler.addItem("BAGLANTILAR YUKLENIYOR")
            else:
                self.splashpencere.listWidgetIslemler.addItem("!!! BAGLANTILARDA HATA MEVCUT")
        if ilerleme == 21:
            self.splashpencere.label_description.setText("ROBOT PLC CONNECTION CONTROL")
        if ilerleme == 40:
            self.splashpencere.progressBar.setValue(ilerleme)
            if durum:
                self.splashpencere.listWidgetIslemler.addItem("ROBOT PLC BAGLANDI")
            else:
                self.splashpencere.listWidgetIslemler.addItem("!!! ROBOT PLC BAGLANAMADI")

        if ilerleme == 41:
            self.splashpencere.label_description.setText("STREC CIKIS PLC CONNECTION CONTROL")
        if ilerleme == 60:
            self.splashpencere.progressBar.setValue(ilerleme)
            if durum:
                self.splashpencere.listWidgetIslemler.addItem("STREC CIKIS PLC BAGLANDI")
            else:
                self.splashpencere.listWidgetIslemler.addItem("!!! STREC CIKIS PLC BAGLANAMADI")

        if ilerleme == 61:
            self.splashpencere.label_description.setText("DATABASE CONNECTING")
        if ilerleme == 80:
            self.splashpencere.progressBar.setValue(ilerleme)
            if durum == 0:
                self.splashpencere.listWidgetIslemler.addItem("DATABASE BAGLANDI")
            else:
                self.splashpencere.listWidgetIslemler.addItem("!!! DATABASE BAGLANDI")

        if ilerleme == 100:
            self.splashpencere.progressBar.setValue(ilerleme)
            self.splashpencere.label_description.setText("<strong> CONNECTION CONTROLS FINISHED</strong>")

        if ilerleme == 101:
            self.prograss_thread.anapencere_show()
            self.thread_durdur()
            self.close()


class SplashScreenThreadClass(QtCore.QThread):
    thread_kontrol_sinyal = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super(SplashScreenThreadClass, self).__init__(parent)
        self.anapencere = MainWindow()

    def run(self):
        try:
            sure = 1
            self.thread_kontrol_sinyal.emit(10, True)

            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(20, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(30, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(40, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(50, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(60, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(70, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(80, True)
            time.sleep(sure)
            self.thread_kontrol_sinyal.emit(101, True)

            """
            self.thread_kontrol_sinyal.emit(1, False)
            if self.anapencere.plc_connect():
                self.thread_kontrol_sinyal.emit(20, True)
            else:
                self.thread_kontrol_sinyal.emit(20, False)

            self.thread_kontrol_sinyal.emit(21, False)
            if self.anapencere.rest_api_connect():
                self.thread_kontrol_sinyal.emit(40, True)
            else:
                self.thread_kontrol_sinyal.emit(40, False)

            self.thread_kontrol_sinyal.emit(41, False)
            if self.anapencere.barcode_reader_connect():
                self.thread_kontrol_sinyal.emit(60, True)
            else:
                self.thread_kontrol_sinyal.emit(60, False)

            self.thread_kontrol_sinyal.emit(61, False)

            status = self.anapencere.printer_connect()
            self.thread_kontrol_sinyal.emit(80, status)

            self.thread_kontrol_sinyal.emit(100, False)
            time.sleep(1)
            self.thread_kontrol_sinyal.emit(101, False)
            """
        except:
            pass
        pass

    def anapencere_show(self):
        self.anapencere.show()

"""if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # get the available screens
    screens = QtWidgets.QDesktopWidget().screenCount()

    # if there are more than one screen, move the window to the second screen
    if screens > 1:
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry(1)  # get the geometry of the second screen
        #main_window = SplashScreen()
        main_window = MainWindow()
        main_window.move(screen_geometry.left(), screen_geometry.top())  # move the window to the second screen
        main_window.showFullScreen()  # show the window in full screen on the second screen
        app.setWindowIcon(QtGui.QIcon("datalar/optimak.ico"))
    else:
        #main_window = SplashScreen()
        main_window = MainWindow()
        main_window.show()  # show the window on the primary screen
        app.setWindowIcon(QtGui.QIcon("datalar/optimak.ico"))

    sys.exit(app.exec_())"""

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(QtGui.QIcon("datalar/optimak.ico"))
    pencere = SplashScreen()
    pencere.show()
    sys.exit(app.exec_())