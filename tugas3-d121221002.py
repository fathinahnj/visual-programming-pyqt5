# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
  def __init__(self):
    super().__init__() 
    layout = QHBoxLayout()
    btn1 = QPushButton("button 1")
    btn2 = QPushButton("button 2")
    btn3 = QPushButton("button 3")
    btn4 = QPushButton("button 4")
    layout.addWidget(btn1, 1, Qt.AlignTop)
    layout.addWidget(btn2, 2)
    layout.addWidget(btn3, 2)
    layout.addWidget(btn4, 5, Qt.AlignBottom)
    self.setLayout(layout) # akses QWidget (self), setLayout sesuai dengan "layout"
    
    # kalau pakai MyWindow(QMainWindow), maka harus menggunakan set central widget
    # widget = QWidget()
    # widget.setLayout(layout)
    # self.setCentralWidget(widget)
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 