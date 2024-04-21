# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
main_win = QWidget()
main_win.setWindowTitle('txt_tile')
main_win.resize(400,200)
main_win.move(900,70)
class TestWin(QWidget):
    def __init__(self):
        super(QWidget).__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def self_appear(self):
        pass
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.btn1)
        self.r_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        pass
