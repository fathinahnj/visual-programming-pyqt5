# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() 
    layout = QFormLayout()
    layout.addRow("Nama", QLineEdit())
    layout.addRow("Email", QLineEdit())
    
    # kalau pakai MyWindow(QMainWindow), maka harus menggunakan set central widget
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)
    
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 