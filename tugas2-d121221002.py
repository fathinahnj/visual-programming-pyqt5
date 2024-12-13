# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget

class MyWindow(QWidget):
  def __init__(self):
    super().__init__() 
    layout = QVBoxLayout()
    btn1 = QPushButton("button 1")
    btn2 = QPushButton("button 2")
    btn3 = QPushButton("button 3")
    btn4 = QPushButton("button 4")
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
    self.setLayout(layout) # akses QWidget (self), setLayout sesuai dengan "layout"
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 