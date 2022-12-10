import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QMainWindow, QDialog, QMessageBox, QSpinBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic

from Attributes import Attributes


form_class = uic.loadUiType("main.ui")[0]
form_carInfowindow = uic.loadUiType("carInfo.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        """
        ---------------------------------------------
        이 부분에 시그널을 입력해야 합니다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
        ---------------------------------------------
        """
        self.btn_1.clicked.connect(self.choulbalFunction)
        self.toKyoungyu.clicked.connect(self.btn_main_to_kyoungyu)
        self.btn_2.clicked.connect(self.btn_carInfo)
        self.undo_Btn.clicked.connect()  # Undo 버튼 부분
        print("main window\n")
        print(Attributes.addressList)

    # imnyukButton이 눌리면 작동할 함수
    def choulbalFunction(self):
        # print("btn_1 Clicked")
        global chulbal
        chulbal = self.imnyukchang.text()
        
        if len(Attributes.addressList) != 0:
            QMessageBox.information(self, '출발지 입력', '출발지가 이미 존재합니다.')
            return
        Attributes.addressList.append(chulbal)

        # print(chulbal)
        # chulbal은 출발지 저장창
        # self.labelindi.setText("출발지가 입력되었습니다. 출발지는: "+chulbal+" 입니다.")
        QMessageBox.information(self, '출발지 입력', '출발지가 입력되었습니다. 출발지는: ' + chulbal + ' 입니다.')

    # 다음 페이지로 가는 부분
    def btn_main_to_kyoungyu(self):
        from SecondWindow import secondwindow
        self.hide()  # 메인윈도우 숨김
        self.second = secondwindow()  #
        self.first = WindowClass()  #
        self.second.exec()  # 두번째 창을 닫을 때 까지 기다림

    def btn_carInfo(self):
        self.Info = carInfoWindow()
        self.Info.show()
        
    def resetbtn(self):
        QMessageBox.information(self, '출발지 입력', '' + Attributes.addressList.pop() + ' 가 삭제되었습니다.')
        
        
class carInfoWindow(QDialog, QWidget, form_carInfowindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Horizontal Slider의 시그널 사용
        self.slider_horizontal.valueChanged.connect(self.showHorizontalSliderValue)

        self.finish.clicked.connect(self.Close)


    def showHorizontalSliderValue(self) :
        #Horizontal Slider의 시그널 이용 - Horizontal Slider의 값이 변경되면 Label에 값을 표시
        self.lbl_horizontal.setText(str(self.slider_horizontal.value())+'%')


    def Close(self):
        #차종은 car_type
        #주유 퍼센트는 gas_Persent
        #주행가능거리 can_go_KM
        car_type = self.carType.currentIndex() + 1
        gas_Persent = self.slider_horizontal.value()
        can_go_KM = self.spinBox.value()

        print(car_type)
        print(gas_Persent)
        print(can_go_KM)
        self.close()
