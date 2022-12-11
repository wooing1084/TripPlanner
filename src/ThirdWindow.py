import sys
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QMainWindow, QDialog, QMessageBox, QSpinBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic
from PyQt5.QtGui import *
from Attributes import Attributes
import main_rc

form_thirdwindow = uic.loadUiType("dochak.ui")[0]

class thirdwindow(QDialog, QWidget, form_thirdwindow):
    def __init__(self):
        super(thirdwindow, self).__init__()
        self.setupUi(self)
        self.show()
        # 배경 사진
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("icon/back_1.png")))
        self.setPalette(palette)

        self.btn_1.clicked.connect(self.dochakFunction)
        self.goBack.clicked.connect(self.btn_kyoungyu_to_main)

        self.undo_Btn.clicked.connect(self.UndoFunction)  # Undo 버튼 부분
        self.totheEnd.clicked.connect(self.GoToResult)#결과보기 버튼 클릭시 부분
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

    # undo버트 부르면 작동하는 부분(각 페이지 마다 똑같이 있음)
    def UndoFunction(self):
        if(len(Attributes.addressList) == 0):
            QMessageBox.information(self, '도착지 입력', '리스트가 비어있습니다!')
        else:
            QMessageBox.information(self, '도착지 입력', '' + Attributes.addressList.pop() + ' 가 삭제되었습니다.')
            
    def GoToResult(self):
        from test_api import get_dis_time
        from test_api import get_time
        from test_api import make_matrix
        from TSP_2 import Algorithm
        
        Attributes.n = len(Attributes.addressList)
        
        value = get_time(Attributes.addressList, Attributes.carType)
        get_dis_time(Attributes.addressList, Attributes.carType) # carval은 톨게이트 요금 계산용 차종 정보를 나타내는 코드.
        result = make_matrix(value, Attributes.n)
        
        Attributes.apiResult = result

        #테스트할때 API호출 횟수가 많으니 한번 쓴거 재사용하자
        # result = [[[0, 0], [0, 0], [float('inf'), float('inf')], [float('inf'), float('inf')], [float('inf'), float('inf')]], 
        #           [[0, 0], [0, 0], [3593.688, 33021], [2942.683, 19101], [4649.855, 35813]],
        #           [[float('inf'), float('inf')], [3302.727, 29687], [0, 0], [2575.093, 16188], [3174.58, 31295]], 
        #           [[float('inf'), float('inf')], [1613.749, 18121], [1653.306, 14930], [0, 0], [2861.655, 19150]], 
        #           [[0, 0], [3789.645, 32665], [2731.982, 33745], [3537.67, 18917], [0, 0]]]

        print(result)
        print("\n")

        alg = Algorithm()
        alg.n = Attributes.n + 1
        alg.graph = result
        alg.dp = [[alg.INF] * (1 << alg.n) for _ in range(alg.n)]

        alg.dfs(0,1)
        Attributes.path = alg.printPath(0,1)
    
            
        print(Attributes.path)

        from resultPage import Windows
        self.close()  # 메인윈도우 숨김
        self.result = Windows()  #
        self.result.show()
        
        