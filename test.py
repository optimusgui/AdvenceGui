# import sys
# import pyodbc
# from PyQt5.QtCore import QTimer, Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.label = QLabel('Waiting for value...', self)
#         self.label.setGeometry(50, 50, 200, 50)
#
#         self.timer = QTimer(self)
#         self.timer.setInterval(500)  # milliseconds
#         self.timer.setSingleShot(True)
#         self.timer.timeout.connect(self.check_value)
#
#         self.timer.start()
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('AVES_DATABASE Check')
#         self.show()
#
#     def check_value(self):
#         # Open a connection to the database
#         conn = pyodbc.connect('DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=Veritabani;UID=AVES_TEST;PWD=12345')
#
#         cursor = conn.cursor()
#
#         # Query the database for the value of erp1 where palet_num is 1000
#         cursor.execute('SELECT pc1 FROM AVES_DATABASE WHERE palet_num = 1001')
#         row = cursor.fetchone()
#         if row is not None and row[0] == 1:
#             self.label.setText('True')
#             print("TRueee")
#         else:
#             self.label.setText('False')
#             print("Falseee")
#         # Close the connection to the database
#         cursor.close()
#         conn.close()
#
#         # Stop the timer if it has been executed twice
#         if self.timer.remainingTime() > 0:
#             self.timer.start()
#         else:
#             self.timer.timeout.disconnect()
#             self.timer.deleteLater()
#             QMessageBox.warning(self, 'Timeout', 'The timer has timed out.')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# import pyodbc
# from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
# from PyQt5.QtGui import QFont
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
#
#
# class QueryThread(QThread):
#     value_changed = pyqtSignal(bool)
#
#     def __init__(self, palet_num):
#         super().__init__()
#         self.palet_num = palet_num
#         self.running = True
#
#     def run(self):
#         while self.running:
#             # Open a connection to the database
#             conn = pyodbc.connect('DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=Veritabani;UID=AVES_TEST;PWD=12345')
#             cursor = conn.cursor()
#
#             # Query the database for the value of erp1 where palet_num is self.palet_num
#             cursor.execute('SELECT erp1 FROM AVES_DATABASE WHERE palet_num = ?', self.palet_num)
#             row = cursor.fetchone()
#             value = False
#             if row is not None and row[0] == 1:
#                 value = True
#
#             # Close the connection to the database
#             cursor.close()
#             conn.close()
#
#             self.value_changed.emit(value)
#
#             self.sleep(1)  # Wait for 1 second before querying again
#
#     def stop(self):
#         self.running = False
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.label = QLabel('Waiting for value...', self)
#         self.label.setGeometry(50, 50, 200, 50)
#         font = QFont()
#         font.setPointSize(12)
#         self.label.setFont(font)
#
#         self.palet_num = 1001  # Set the value of palet_num here
#         self.thread = QueryThread(self.palet_num)
#         self.thread.value_changed.connect(self.on_value_changed)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('AVES_DATABASE')
#
#     def showEvent(self, event):
#         self.thread.start()
#
#     def closeEvent(self, event):
#         self.thread.stop()
#
#     def on_value_changed(self, value):
#         if value:
#             self.label.setText('Value is True')
#         else:
#             self.label.setText('Value is False')
#         self.label.repaint()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec_())


import sys
import pyodbc
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox


class QueryThread(QThread):
    value_changed = pyqtSignal(bool)

    def __init__(self, palet_num):
        super().__init__()
        self.palet_num = palet_num

    def run(self):
        # Open a connection to the database
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=aves_database;UID=sa;PWD=mypassword')
        cursor = conn.cursor()

        # Query the database for the value of erp1 where palet_num is self.palet_num
        cursor.execute('SELECT erp1 FROM AVES_DATABASE WHERE palet_num = ?', self.palet_num)
        row = cursor.fetchone()
        value = False
        if row is not None and row[0] == 1:
            value = True

        # Close the connection to the database
        cursor.close()
        conn.close()

        self.value_changed.emit(value)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Waiting for value...', self)
        self.label.setGeometry(50, 50, 200, 50)
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.palet_num = 1000  # Set the value of palet_num here
        self.thread = QueryThread(self.palet_num)
        self.thread.value_changed.connect(self.on_value_changed)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('AVES_DATABASE')

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.thread.start)
        self.timer.start(500)  # Start the timer after 0.5 seconds

    def on_value_changed(self, value):
        if value:
            self.label.setText('Value is True')
        else:
            self.label.setText('Value is False')
        self.label.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

