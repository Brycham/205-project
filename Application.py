'''
    
    Author: Luis Alva
    
    Description: This is the application window that will call other files in the same directory and put the images accordingly to where they need to be. 
    
    
    '''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QInputDialog, QFileDialog, QComboBox, QLineEdit, QHBoxLayout
from PyQt5.QtCore import pyqtSlot
import PastMust as reco
import reco as recognize

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, QUrl

from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

temp = ""
temp1 = ""

temp2 = ""

my_list = ["Face", "Mouth", "Eyes"]

class NewWindow1(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle('Image Manipulation')
        
        qbox = QVBoxLayout()
        
        
        
        self.label1 = QLabel('Choose your images to Plaster')
        self.btn = QPushButton("Choose Face(s)", self)
        self.btn1 = QPushButton("Choose a Mustache", self)
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
    
    
    def crop(self,sentence):
        path = ""
        for letter in sentence:
            if(letter == "/"):
                path = ""
            else:
                path += letter
        return path
    
    def on_click2(self):
        reco.pastFunction(temp, temp1)
    
    
    
    
    
    def on_click(self):
       
        global temp
        temp = self.openFileNameDialog()
        tempi = self.crop(temp)
        self.btn.setText(tempi)
     
     

    
    def on_click1(self):
        global temp1
        temp1 = self.openFileNameDialog()
        tempi = self.crop(temp1)
        self.btn1.setText(tempi)
    
    




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
        
        

        self.setWindowTitle('Face Recognition')
        
        qbox = QVBoxLayout()
        
        global my_list
        
        self.my_combo_box = QComboBox()
        
        self.my_combo_box.addItems(my_list)
        
        self.label1 = QLabel('Choose your Face(s)')
      
        self.btn = QPushButton("Choose a Face(s)", self)
        self.btn1 = QPushButton("Run", self)
        
        
        qbox.addWidget(self.label1)
        qbox.addWidget(self.btn)
        qbox.addWidget(self.my_combo_box)
        qbox.addWidget(self.btn1)
        
        self.btn.clicked.connect(self.on_click)
        self.btn1.clicked.connect(self.on_click4)
        
        self.setLayout(qbox)
    
    
    
    def crop(self,sentence):
        path = ""
        for letter in sentence:
            if(letter == "/"):
                path = ""
            else:
                path += letter
        return path
    
    
    def on_click(self):
        global temp2
        temp2 = self.openFileNameDialog()
        tempi = self.crop(temp2)
        self.btn.setText(tempi)
    
    
    
    def on_click4(self):
        global temp2
        if(self.my_combo_box.currentText()=="Face"):
            recognize.recognize(temp2)
#        elif(self.my_combo_box.currentText()=="Mouth"):
#            
#        elif(self.my_combo_box.currentText()=="Eyes"):


    
    
    
    



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
        
        #self.my_combo_box = QComboBox()
        
        self.label1 = QLabel('Which would you like to do?')
        
        self.my_btn = QPushButton("Facial Recognize", self)
        self.my_btn1 = QPushButton("Plaster", self)
        
        vbox.addWidget(self.label1)
        
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_btn1)
        #vbox.addWidget(self.my_combo_box)
        
        self.my_btn.clicked.connect(self.on_click)
        self.my_btn1.clicked.connect(self.on_click1)
        
        self.setLayout(vbox)
    
    





    #@pyqtSlot()
    def on_click(self):
        
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
