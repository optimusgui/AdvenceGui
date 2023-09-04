import os

try:
    os.system("python -m PyQt5.uic.pyuic -x MainWindow.ui -o ui_MainWindow.py")
    os.system("python -m PyQt5.uic.pyuic -x SplashWindow.ui -o ui_SplashWindow.py")

    os.system("Pyrcc5 ikonlar.qrc -o ikonlar_rc.py")

except Exception as e:
    print(e)
    pass
