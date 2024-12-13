# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() 
    layout = QVBoxLayout()
    btn1 = QPushButton("button 1")
    btn2 = QPushButton("button 2")
    btn3 = QPushButton("button 3")
    btn4 = QPushButton("button 4")
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 