# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFormLayout, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() 
    layout = QFormLayout()
    
    # kalau pakai MyWindow(QMainWindow), maka harus menggunakan set central widget
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 