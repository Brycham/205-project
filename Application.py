import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QInputDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot
import reco as recognize

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, QUrl

from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

temp = ""
temp1 = ""

class NewWindow1(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle('Image Manipulation')
        
        qbox = QVBoxLayout()
        
        
        self.label1 = QLabel('Choose your images to Plaster')
        self.btn = QPushButton("Choose Image", self)
        self.btn1 = QPushButton("Choose Image", self)
        self.btn2 = QPushButton("Run", self)
     
        
        
        qbox.addWidget(self.label1)
        qbox.addWidget(self.btn)
        qbox.addWidget(self.btn1)
        qbox.addWidget(self.btn2)

        self.btn.clicked.connect(self.on_click)
        self.btn1.clicked.connect(self.on_click1)
        
        self.btn2.clicked.connect(self.on_click2)
        #Maybe make a global variable with the temp that will store it so i dont worry about returning.
        self.setLayout(qbox)
    
    
    def on_click2(self):
        print(temp)
        print(temp1)
    
    
    
    
    def on_click(self):
        global temp
        temp = self.openFileNameDialog()

    
    def on_click1(self):
        global temp1
        temp1 = self.openFileNameDialog()



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName



class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle('Face Warp')
        
        qbox = QVBoxLayout()
        
        
        self.label1 = QLabel('Choose your images')
        self.btn = QPushButton("Choose Image", self)
        
        
        qbox.addWidget(self.label1)
        qbox.addWidget(self.btn)
        
        self.btn.clicked.connect(self.on_click)
        self.setLayout(qbox)
    
    
    def on_click(self):
        recognize.recognize(self.openFileNameDialog())
    
    



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName


#self.load()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Face Manipulation')
        
        vbox = QVBoxLayout()
        
        self.my_combo_box = QComboBox()
        self.label1 = QLabel('Which would you like to do?')
        
        self.my_btn = QPushButton("Face Warp", self)
        self.my_btn1 = QPushButton("Plaster", self)
        
        vbox.addWidget(self.label1)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_btn1)
        
        self.my_btn.clicked.connect(self.on_click)
        self.my_btn1.clicked.connect(self.on_click1)
        
        self.setLayout(vbox)
    
    





    #@pyqtSlot()
    def on_click(self):
        
        # i = self.my_combo_box.currentIndex()
        # if i!=0:
        self.new_win = NewWindow()
        self.new_win.show()

    def on_click1(self):
        self.new_win = NewWindow1()
        self.new_win.show()


#recognize.recognize(self.openFileNameDialog())










mainWin = MainWindow()
mainWin.show()
status = app.exec_()
sys.exit(status)
