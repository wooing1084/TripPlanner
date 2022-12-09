import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QMainWindow, QDialog, QMessageBox, QSpinBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main.ui")[0]

form_secondwindow = uic.loadUiType("kyoungyu.ui")[0]

form_thirdwindow = uic.loadUiType("dochak.ui")[0]

form_carInfowindow = uic.loadUiType("carInfo.ui")[0]

#######################################################
global chulbal
global dochak
global kNum
global kList
kNum = 0
kList = []


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

    # imnyukButton이 눌리면 작동할 함수
    def choulbalFunction(self):
        # print("btn_1 Clicked")
        global chulbal
        chulbal = self.imnyukchang.text()

        # print(chulbal)
        # chulbal은 출발지 저장창
        # self.labelindi.setText("출발지가 입력되었습니다. 출발지는: "+chulbal+" 입니다.")
        QMessageBox.information(self, '출발지 입력', '출발지가 입력되었습니다. 출발지는: ' + chulbal + ' 입니다.')

    # 다음 페이지로 가는 부분
    def btn_main_to_kyoungyu(self):
        self.hide()  # 메인윈도우 숨김
        self.second = secondwindow()  #
        self.first = WindowClass()  #
        self.second.exec()  # 두번째 창을 닫을 때 까지 기다림

    def btn_carInfo(self):
        self.Info = carInfoWindow()
        self.Info.show()


class carInfoWindow(QDialog, QWidget, form_carInfowindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.carType.currentIndexChanged.connect()

        self.finish.clicked.connect(self.Close)

    def Close(self):
        self.close()


class secondwindow(QDialog, QWidget, form_secondwindow):
    def __init__(self):
        super(secondwindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.btn_1.clicked.connect(self.kyoungyuFunction)

        self.goBack.clicked.connect(self.btn_kyoungyu_to_main)
        self.toDochak.clicked.connect(self.btn_main_to_dochak)

    # imnyukButton이 눌리면 작동할 함수
    def kyoungyuFunction(self):
        global kNum
        global kList
        if kNum == 10:
            QMessageBox.information(self, '경유지 입력 초과', '더이상 경유지를 입력할 수 없습니다. 도착지 입력을 눌러주세요')
        # print("btn_1 Clicked")
        kyoungyu = self.imnyukchang.text()

        kList.insert(0, kyoungyu)
        # print(kyoungyu)
        # kyoungyu 출발지 저장창
        # self.labelindi.setText("출발지가 입력되었습니다. 출발지는: "+kyoungyu+" 입니다.")

        if kNum == 0:
            QMessageBox.information(self, '경유지 입력', '첫번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 1:
            QMessageBox.information(self, '경유지 입력', '두번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 2:
            QMessageBox.information(self, '경유지 입력', '세번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 3:
            QMessageBox.information(self, '경유지 입력', '네번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 4:
            QMessageBox.information(self, '경유지 입력', '다섯번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 5:
            QMessageBox.information(self, '경유지 입력', '여섯번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 6:
            QMessageBox.information(self, '경유지 입력', '일곱번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 7:
            QMessageBox.information(self, '경유지 입력', '여덟번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 8:
            QMessageBox.information(self, '경유지 입력', '아홉번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')
        if kNum == 9:
            QMessageBox.information(self, '경유지 입력', '열번째 경유지가 입력되었습니다. 경유지는: ' + kList[kNum] + ' 입니다.')

        self.imnyukchang.clear()

        '''
        i = kNum + 1
        for i in kList:
            print(i)
        '''

    def btn_kyoungyu_to_main(self):
        self.close()  # 클릭시 종료됨.
        self.first = WindowClass()  #
        self.first.show()  # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

    # 다음 페이지로 가는 부분
    def btn_main_to_dochak(self):
        self.hide()  # 메인윈도우 숨김
        self.third = thirdwindow()  #
        self.third.exec()  # 두번째 창을 닫을 때 까지 기다림


class thirdwindow(QDialog, QWidget, form_thirdwindow):
    def __init__(self):
        super(thirdwindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.btn_1.clicked.connect(self.dochakFunction)
        self.goBack.clicked.connect(self.btn_kyoungyu_to_main)

        # imnyukButton이 눌리면 작동할 함수

    def dochakFunction(self):
        # print("btn_1 Clicked")
        global dochak
        dochak = self.imnyukchang.text()

        # print(dochak)
        # dochak 도착지 저장창
        # self.labelindi.setText("출발지가 입력되었습니다. 출발지는: "+chulbal+" 입니다.")
        QMessageBox.information(self, '도착지 입력', '도착지가 입력되었습니다. 도착지는: ' + dochak + ' 입니다.')

    def btn_kyoungyu_to_main(self):
        self.close()  # 클릭시 종료됨.
        self.second = secondwindow()  #
        self.second.show()  # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
