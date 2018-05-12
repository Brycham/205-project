import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QInputDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap


app = QApplication(sys.argv)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image Manipulation')
        
        vbox = QVBoxLayout()
        
        self.my_combo_box = QComboBox()
        self.label1 = QLabel('Which would you like to do?')
        
        self.my_btn = QPushButton("Face Warp", self)
        self.my_btn1 = QPushButton("Plaster", self)
        
        vbox.addWidget(self.label1)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_btn1)
        
        self.my_btn.clicked.connect(self.on_click)
        # self.my_btn1.clicked.connect(self.on_click1)
        
        self.setLayout(vbox)




mainWin = MainWindow()
mainWin.show()
status = app.exec_()
sys.exit(status)
