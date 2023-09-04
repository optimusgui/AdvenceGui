from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import win32print
import win32api
import time
import os
import codecs
from PyQt5.QtCore import *

PRINTER_ERROR_STATES = (
    win32print.PRINTER_STATUS_BUSY,
    win32print.PRINTER_STATUS_DOOR_OPEN,
    win32print.PRINTER_STATUS_ERROR,
    win32print.PRINTER_STATUS_INITIALIZING,
    win32print.PRINTER_STATUS_IO_ACTIVE,
    win32print.PRINTER_STATUS_MANUAL_FEED,
    win32print.PRINTER_STATUS_NOT_AVAILABLE,
    win32print.PRINTER_STATUS_NO_TONER,
    win32print.PRINTER_STATUS_OFFLINE,
    win32print.PRINTER_STATUS_OUTPUT_BIN_FULL,
    win32print.PRINTER_STATUS_OUT_OF_MEMORY,
    win32print.PRINTER_STATUS_PAGE_PUNT,
    win32print.PRINTER_STATUS_PAPER_JAM,
    win32print.PRINTER_STATUS_PAPER_OUT,
    win32print.PRINTER_STATUS_PAPER_PROBLEM,
    win32print.PRINTER_STATUS_PAUSED,
    win32print.PRINTER_STATUS_PENDING_DELETION,
    win32print.PRINTER_STATUS_POWER_SAVE,
    win32print.PRINTER_STATUS_PRINTING,
    win32print.PRINTER_STATUS_PROCESSING,
    win32print.PRINTER_STATUS_SERVER_UNKNOWN,
    win32print.PRINTER_STATUS_TONER_LOW,
    win32print.PRINTER_STATUS_USER_INTERVENTION,
    win32print.PRINTER_STATUS_WAITING,
    win32print.PRINTER_STATUS_WARMING_UP,
)
PRINTER_ERROR_STATES_DICT = {
    "PRINTER_STATUS_BUSY": 512,
    "PRINTER_STATUS_DOOR_OPEN": 4194304,
    "PRINTER_STATUS_ERROR": 2,
    "PRINTER_STATUS_INITIALIZING": 32768,
    "PRINTER_STATUS_IO_ACTIVE": 256,
    "PRINTER_STATUS_MANUAL_FEED": 32,
    "PRINTER_STATUS_NOT_AVAILABLE": 4096,
    "PRINTER_STATUS_NO_TONER": 262144,
    "PRINTER_STATUS_OFFLINE": 128,
    "PRINTER_STATUS_OUTPUT_BIN_FULL": 2048,
    "PRINTER_STATUS_OUT_OF_MEMORY": 2097152,
    "PRINTER_STATUS_PAGE_PUNT": 524288,
    "PRINTER_STATUS_PAPER_JAM": 8,
    "PRINTER_STATUS_PAPER_OUT": 16,
    "PRINTER_STATUS_PAPER_PROBLEM": 64,
    "PRINTER_STATUS_PAUSED": 1,
    "PRINTER_STATUS_PENDING_DELETION": 4,
    "PRINTER_STATUS_POWER_SAVE": 16777216,
    "PRINTER_STATUS_PRINTING": 1024,
    "PRINTER_STATUS_PROCESSING": 16384,
    "PRINTER_STATUS_SERVER_UNKNOWN": 8388608,
    "PRINTER_STATUS_TONER_LOW": 131072,
    "PRINTER_STATUS_USER_INTERVENTION": 1048576,
    "PRINTER_STATUS_WAITING": 8192,
    "PRINTER_STATUS_WARMING_UP": 65536,
}

def musteri_etiketi_olustur(etiket_verisi, dosya_adi):
    try:
        document = DocxTemplate(f"formlar/{dosya_adi}.docx")
        context2 = {
            'v': etiket_verisi,
        }
        document.render(context2)
        document.save(f"form_outputs/{dosya_adi}_output.docx")
        return True, f"{dosya_adi}_output.docx"

    except Exception as e:
        return False, str(e)


def form_print(printer_name, file_name):
    try:
        os.chdir("form_outputs/")
        os.system(f'RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "{printer_name}" ')
        win32api.ShellExecute(0, "printto", file_name, f'"{printer_name}"', ".", 0)
        os.chdir("..")
        return True, "PRINT STARTED"
    except Exception as e:
        return False, str(e)
        pass

def form_print_old(printer_name, file_name):
    try:
        time.sleep(1.5)
        win32print.SetDefaultPrinter(printer_name)
        hPrinter = win32print.OpenPrinter(printer_name)
        PrinterStatus, PrinterStatusStr = printer_errorneous_state(hPrinter)
        if PrinterStatus == 0:
            os.chdir("form_outputs/")
            os.startfile('{}'.format(file_name), "print")
            os.chdir("..")
            time.sleep(0.5)
            PrinterStatus, PrinterStatusStr = printer_errorneous_state(hPrinter)
            if PrinterStatus == 0 or PrinterStatus == 1024:
                return True, PrinterStatusStr
            elif PrinterStatus != 0 or PrinterStatus != 1024:
                return False, PrinterStatusStr
            return True, PrinterStatusStr
        else:
            return False, PrinterStatusStr
    except Exception as e:
        return False, str(e)


def printer_errorneous_state(printer, error_states=PRINTER_ERROR_STATES):
    prn_opts = win32print.GetPrinter(printer)
    status_opts = prn_opts[18]
    error_state_string = "ONLINE"
    for error_state in error_states:
        if status_opts & error_state:
            for hata_adi, hata_kodu in PRINTER_ERROR_STATES_DICT.items():
                if hata_kodu == error_state:
                    error_state_string = hata_adi
                    break
            return error_state, error_state_string
    return 0, error_state_string

def get_printer_list():
    gidecek_liste = []
    default_printer_name = win32print.GetDefaultPrinter()
    gidecek_liste.append(default_printer_name)
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS + win32print.PRINTER_ENUM_LOCAL)
    for printer in printers:
        if printer[2] == default_printer_name:
            continue
        gidecek_liste.append(str(printer[2]))
    return gidecek_liste

class ThreadClassPrinterControl(QThread):
    yazicilarStatusSinyal = pyqtSignal(int, str, int, str, int, str)

    def __init__(self, YAZICI_HAT_1, YAZICI_HAT_2, YAZICI_HAT_3, parent=None):
        super(ThreadClassPrinterControl, self).__init__(parent)
        try:
            self.hPrinterHat_1 = win32print.OpenPrinter(YAZICI_HAT_1)
            self.hPrinterHat_2 = win32print.OpenPrinter(YAZICI_HAT_2)
            self.hPrinterHat_3 = win32print.OpenPrinter(YAZICI_HAT_3)
        except Exception as Hata:
            print(Hata)
            pass

    def run(self):
        while True:
            time.sleep(0.2)
            try:
                yaziciHat_1Status, yaziciHat_1Str = printer_errorneous_state(self.hPrinterHat_1)
                yaziciHat_2Status, yaziciHat_2Str = printer_errorneous_state(self.hPrinterHat_2)
                yaziciHat_3Status, yaziciHat_3Str = printer_errorneous_state(self.hPrinterHat_3)

                self.yazicilarStatusSinyal.emit(yaziciHat_1Status, yaziciHat_1Str, yaziciHat_2Status,
                                                yaziciHat_2Str, yaziciHat_3Status, yaziciHat_3Str)
            except Exception as e:
                print("ThreadClassPrinterControl run exception: ", str(e))
                pass
            pass

    def ayar_transfer(self, yazici_Hat_1, yazici_Hat_2, yazici_Hat_3):
        try:
            win32print.ClosePrinter(self.hPrinterHat_1)
            win32print.ClosePrinter(self.hPrinterHat_2)
            win32print.ClosePrinter(self.hPrinterHat_3)

            self.hPrinterHat_1 = win32print.OpenPrinter(yazici_Hat_1)
            self.hPrinterHat_2 = win32print.OpenPrinter(yazici_Hat_2)
            self.hPrinterHat_3 = win32print.OpenPrinter(yazici_Hat_3)
        except Exception as e:
            print("ThreadClassPrinterControl run exception: ", str(e))
            pass
