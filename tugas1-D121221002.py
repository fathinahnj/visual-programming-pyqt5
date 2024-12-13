# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QWidget, QDesktopWidget
from PyQt5 import QtCore 

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
    
    # memindahkan ke tengah windows
    cwa = self.frameGeometry()
    cwc = QDesktopWidget().availableGeometry().center()
    cwa.moveCenter(cwc)
    self.move(cwa.topLeft())
    self.setFixedSize(500,500)
    # menghilangkan salah satu tombol di kanan atas
    # self.setWindowFlag(QtCore.Qt.FramelessWindowHint) 
    # self.setWindowFlag(QtCore.Qt.WindowMinimizedButtonHint,False)
    # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint,False) 

app = QApplication([])
window = MyWindow()
window.show()
app.exec() 