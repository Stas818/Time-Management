import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import (QDateTime, QUrl, Qt, QTimer, QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox, QMainWindow)
from PyQt5.QtGui import (QPalette, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Time Manager")
        self.TitleLabel = QtWidgets.QLabel(MainWindow)
        self.TitleLabel.move(800, 800)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(36)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.webView = QtWebEngineWidgets.QWebEngineView(MainWindow)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.LabelTitle(MainWindow)
        self.TitleLabel.update
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def LabelTitle(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Welcome to Time Management"))
        self.TitleLabel.update

    def update(self):
        self.label.adjustSize()

if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    MainWindow = qtw.QMainWindow()
    mw = Ui_MainWindow()
    mw.setupUi(MainWindow)
    view = MainWindow.showMaximized()
    sys.exit(app.exec_())
