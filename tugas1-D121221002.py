# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QWidget

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() 
    # window = QMainWindow()
    # window = QPushButton("Fathinah Nur Jannah_D121221002")
    self.label = QLabel(self) # membungkus window (button fathin) di dalam label
    self.label.setText("Label 1") # menamai label
    self.label.move(200, 10) # posisi dari tulisan "label 1"
    self.button = QPushButton(self) # menambahkan button di dalam window (button fathin)
    self.button.setText("Button 1") # menuliskan button di dalam window 
    
    self.setGeometry(0, 0, 500, 500) # set posisi (x, y, width, height) dari MyWindow
    self.setWindowTitle("Belajar PyQt5") # set judul dari windows yang terbuka untuk MyWindow


app = QApplication([])
window = MyWindow()
window.show()
app.exec() 