import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QMainWindow, QDialog, QMessageBox, QSpinBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic

from Attributes import Attributes

form_thirdwindow = uic.loadUiType("src/dochak.ui")[0]

class thirdwindow(QDialog, QWidget, form_thirdwindow):
    def __init__(self):
        super(thirdwindow, self).__init__()
        self.setupUi(self)
        self.show()


        self.btn_1.clicked.connect(self.dochakFunction)
        self.goBack.clicked.connect(self.btn_kyoungyu_to_main)
        self.undo_Btn.clicked.connect()#Undo 버튼 부분

        self.totheEnd.clicked.connect()#결과보기 버튼 클릭시 부분
        print("Destination input window!\n")
        print(Attributes.addressList)

        # imnyukButton이 눌리면 작동할 함수

    def dochakFunction(self):
        # print("btn_1 Clicked")
        global dochak
        dochak = self.imnyukchang.text()

        Attributes.addressList.append(dochak)
        # print(dochak)
        # dochak 도착지 저장창
        # self.labelindi.setText("출발지가 입력되었습니다. 출발지는: "+chulbal+" 입니다.")
        QMessageBox.information(self, '도착지 입력', '도착지가 입력되었습니다. 도착지는: ' + dochak + ' 입니다.')

    def btn_kyoungyu_to_main(self):
        from SecondWindow import secondwindow
        self.close()  # 클릭시 종료됨.
        self.second = secondwindow()  #
        self.second.show()  # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐