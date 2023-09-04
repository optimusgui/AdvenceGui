import os

try:
    os.system("python -m PyQt5.uic.pyuic -x GUI/MainWindow.ui -o GUI_PY/ui_MainWindow.py")
    os.system("python -m PyQt5.uic.pyuic -x GUI/SplashWindow.ui -o GUI_PY/ui_SplashWindow.py")
    os.system("python -m PyQt5.uic.pyuic -x GUI/PLC.ui -o GUI_PY/ui_PLC.py")
    os.system("python -m PyQt5.uic.pyuic -x GUI/Ayarlar.ui -o GUI_PY/ui_Ayarlar.py")
    os.system("python -m PyQt5.uic.pyuic -x GUI/Ayarlar_Kamera.ui -o GUI_PY/ui_Ayarlar_Kamera.py")
    
    os.system("Pyrcc5 ikonlar.qrc -o ikonlar_rc.py")

except Exception as e:
    print(e)
    pass
