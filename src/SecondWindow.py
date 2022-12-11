import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QMainWindow, QDialog, QMessageBox, QSpinBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic

from Attributes import Attributes
import main_rc





form_secondwindow = uic.loadUiType("kyoungyu.ui")[0]

class secondwindow(QDialog, QWidget, form_secondwindow):
    kNum = 0
    kList = []
    def __init__(self):
        super(secondwindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.btn_1.clicked.connect(self.kyoungyuFunction)

        self.goBack.clicked.connect(self.btn_kyoungyu_to_main)
        self.toDochak.clicked.connect(self.btn_main_to_dochak)
        self.undo_Btn.clicked.connect(self.UndoFunction)  # Undo 버튼 부분
        print("Second window show\n")
        print(Attributes.addressList)

    # imnyukButton이 눌리면 작동할 함수

    def kyoungyuFunction(self):
        if self.kNum == 10:
            QMessageBox.information(self, '경유지 입력 초과', '더이상 경유지를 입력할 수 없습니다. 도착지 입력을 눌러주세요')
        # print("btn_1 Clicked")
        kyoungyu = self.imnyukchang.text()

        self.kList.append(kyoungyu)
        Attributes.addressList.append(kyoungyu)
        # print(kyoungyu)
        # kyoungyu 출발지 저장창
        # self.labelindi.setText("출발지가 입력되었습니다. 출발지는: "+kyoungyu+" 입니다.")

        if self.kNum == 0:
            QMessageBox.information(self, '경유지 입력', '첫번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 1:
            QMessageBox.information(self, '경유지 입력', '두번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 2:
            QMessageBox.information(self, '경유지 입력', '세번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 3:
            QMessageBox.information(self, '경유지 입력', '네번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 4:
            QMessageBox.information(self, '경유지 입력', '다섯번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 5:
            QMessageBox.information(self, '경유지 입력', '여섯번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 6:
            QMessageBox.information(self, '경유지 입력', '일곱번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 7:
            QMessageBox.information(self, '경유지 입력', '여덟번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 8:
            QMessageBox.information(self, '경유지 입력', '아홉번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
        if self.kNum == 9:
            QMessageBox.information(self, '경유지 입력', '열번째 경유지가 입력되었습니다. 경유지는: ' + self.kList[self.kNum] + ' 입니다.')
            
        self.kNum += 1

        self.imnyukchang.clear()

        '''
        i = kNum + 1
        for i in kList:
            print(i)
        '''

    def btn_kyoungyu_to_main(self):
        from Main_Form import WindowClass
        self.close()  # 클릭시 종료됨.
        self.first = WindowClass()  #
        self.first.show()  # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

    # 다음 페이지로 가는 부분
    def btn_main_to_dochak(self):
        from ThirdWindow import thirdwindow
        self.hide()  # 메인윈도우 숨김
        self.third = thirdwindow()  #
        self.third.exec()  # 두번째 창을 닫을 때 까지 기다림

    # undo버트 부르면 작동하는 부분(각 페이지 마다 똑같이 있음)
    def UndoFunction(self):
        if(len(Attributes.addressList) == 0):
            QMessageBox.information(self, '경유지 입력', '리스트가 비어있습니다!')
        else:
            QMessageBox.information(self, '경유지 입력', '' + Attributes.addressList.pop() + ' 가 삭제되었습니다.')
