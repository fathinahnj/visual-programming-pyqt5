# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGridLayout, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
  def __init__(self):
    super().__init__() 
    layout = QGridLayout()
    btn1 = QPushButton("baris 0 kolom 0")
    btn2 = QPushButton("baris 0 kolom 1")
    btn3 = QPushButton("baris 1 kolom 0")
    btn4 = QPushButton("baris 1 kolom 1")
    layout.addWidget(btn1, 0, 0)
    layout.addWidget(btn2, 0, 1)
    layout.addWidget(btn3, 1, 0)
    layout.addWidget(btn4, 1, 1)
    self.setLayout(layout) # akses QWidget (self), setLayout sesuai dengan "layout"
    
    # Perbedaan antara QH dan QV box alignment adalah di QH ada "stretch" dan "alignment"
    
    # kalau pakai MyWindow(QMainWindow), maka harus menggunakan set central widget
    # widget = QWidget()
    # widget.setLayout(layout)
    # self.setCentralWidget(widget)
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 