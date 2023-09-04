# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/SplashWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(770, 553)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.robot_border_frame = QtWidgets.QFrame(self.centralwidget)
        self.robot_border_frame.setGeometry(QtCore.QRect(540, 0, 221, 201))
        self.robot_border_frame.setStyleSheet("border:7px solid rgb(0, 119, 238);\n"
"border-radius: 20px;\n"
"background-color: rgb(236, 236, 236);")
        self.robot_border_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robot_border_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robot_border_frame.setObjectName("robot_border_frame")
        self.optimak_logo_frame = QtWidgets.QFrame(self.centralwidget)
        self.optimak_logo_frame.setGeometry(QtCore.QRect(122, 115, 561, 361))
        self.optimak_logo_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.017, x2:1, y2:0.965864, stop:0 rgba(101, 101, 135, 255), stop:1 rgba(101, 101, 135, 255));\n"
"border-radius: 30px;")
        self.optimak_logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.optimak_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optimak_logo_frame.setObjectName("optimak_logo_frame")
        self.logo_frame = QtWidgets.QFrame(self.optimak_logo_frame)
        self.logo_frame.setGeometry(QtCore.QRect(20, 50, 491, 141))
        self.logo_frame.setStyleSheet("image: url(:/ikonlar/icons/optimus_logo.png);\n"
"background-color:none;")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.information_frame = QtWidgets.QFrame(self.optimak_logo_frame)
        self.information_frame.setGeometry(QtCore.QRect(130, 210, 431, 151))
        self.information_frame.setStyleSheet("background-color: rgb(173, 173, 229);\n"
"border-radius: 20px;\n"
"border: 7px solid rgb(130, 130, 173);")
        self.information_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.information_frame.setObjectName("information_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.information_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_description = QtWidgets.QLabel(self.information_frame)
        self.label_description.setStyleSheet("background-color: none;\n"
"border: none;\n"
"font: 8pt \"Siemens Sans Black\";")
        self.label_description.setText("")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.progressBar = QtWidgets.QProgressBar(self.information_frame)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(221, 221, 221);\n"
"    border:3px solid rgb(87, 87, 117);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.933, y1:0.892045, x2:1, y2:1, stop:0 rgba(22, 238, 22, 206), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.progressBar.setProperty("value", 5)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.listWidgetIslemler = QtWidgets.QListWidget(self.information_frame)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidgetIslemler.setFont(font)
        self.listWidgetIslemler.setStyleSheet("border: none;\n"
"font: 7pt \"Franklin Gothic Demi Cond\";")
        self.listWidgetIslemler.setObjectName("listWidgetIslemler")
        self.verticalLayout.addWidget(self.listWidgetIslemler)
        self.robot_image_frame = QtWidgets.QFrame(self.centralwidget)
        self.robot_image_frame.setGeometry(QtCore.QRect(532, 17, 232, 171))
        self.robot_image_frame.setStyleSheet("image: url(:/ikonlar/icons/ROBOT_VE_URUNLER.png);")
        self.robot_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robot_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robot_image_frame.setObjectName("robot_image_frame")
        self.pushButtonCancel = QtWidgets.QPushButton(self.robot_image_frame)
        self.pushButtonCancel.setGeometry(QtCore.QRect(200, 0, 21, 21))
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(236, 236, 236);\n"
"image: none;\n"
"border-radius:10px;")
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.makine_frame = QtWidgets.QFrame(self.centralwidget)
        self.makine_frame.setGeometry(QtCore.QRect(0, 305, 291, 221))
        self.makine_frame.setStyleSheet("image: url(:/ikonlar/icons/strech_removed.png);")
        self.makine_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.makine_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.makine_frame.setObjectName("makine_frame")
        self.makine_border_frame = QtWidgets.QFrame(self.centralwidget)
        self.makine_border_frame.setGeometry(QtCore.QRect(2, 295, 311, 251))
        self.makine_border_frame.setStyleSheet("border:7px solid  rgb(0, 75, 156);\n"
"border-radius: 20px;\n"
"background-color: rgb(236, 236, 236);\n"
"")
        self.makine_border_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.makine_border_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.makine_border_frame.setObjectName("makine_border_frame")
        self.labelSoftwareVersion = QtWidgets.QLabel(self.centralwidget)
        self.labelSoftwareVersion.setGeometry(QtCore.QRect(320, 480, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSoftwareVersion.setFont(font)
        self.labelSoftwareVersion.setStyleSheet("background-color: none;")
        self.labelSoftwareVersion.setText("")
        self.labelSoftwareVersion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSoftwareVersion.setObjectName("labelSoftwareVersion")
        self.makine_border_frame.raise_()
        self.robot_border_frame.raise_()
        self.optimak_logo_frame.raise_()
        self.makine_frame.raise_()
        self.robot_image_frame.raise_()
        self.labelSoftwareVersion.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.pushButtonCancel.setText(_translate("SplashScreen", "x"))
import ikonlar_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
