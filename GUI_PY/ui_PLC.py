# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/PLC.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PLC(object):
    def setupUi(self, PLC):
        PLC.setObjectName("PLC")
        PLC.resize(800, 590)
        self.centralwidget = QtWidgets.QWidget(PLC)
        self.centralwidget.setObjectName("centralwidget")
        PLC.setCentralWidget(self.centralwidget)

        self.retranslateUi(PLC)
        QtCore.QMetaObject.connectSlotsByName(PLC)

    def retranslateUi(self, PLC):
        _translate = QtCore.QCoreApplication.translate
        PLC.setWindowTitle(_translate("PLC", "PLC Ayarlar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PLC = QtWidgets.QMainWindow()
    ui = Ui_PLC()
    ui.setupUi(PLC)
    PLC.show()
    sys.exit(app.exec_())
