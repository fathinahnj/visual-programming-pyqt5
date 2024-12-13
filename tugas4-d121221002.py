# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGridLayout, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
  def __init__(self):
    super().__init__() 
    layout = QGridLayout()
    btn1 = QPushButton("button 1")
    btn2 = QPushButton("button 2")
    btn3 = QPushButton("button 3")
    btn4 = QPushButton("button 4")
    layout.addWidget(btn1, 0, 0)
    layout.addWidget(btn2, 0, 1)
    layout.addWidget(btn3, 0, 2)
    layout.addWidget(btn4, 1, 0, 1, 3) # mengambil 3 kolom
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