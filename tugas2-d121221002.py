# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() 
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 