import sys
import folium
import webview
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QMainWindow, QDialog, QMessageBox, QSpinBox, QComboBox, QLabel, QListWidgetItem)
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_rc

from Attributes import Attributes

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("end.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class Windows(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        """
        ---------------------------------------------
        이 부분에 시그널을 입력해야 합니다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
        ---------------------------------------------
        """


    def __init__(self):
        super(Windows, self).__init__()
        self.setupUi(self)
        # 배경 사진
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("icon/back_1.png")))
        self.setPalette(palette)
        #버튼을 누르면 결과값을 출력
        self.pushButton.clicked.connect(self.deal)

        #아래부턴 디자이너의 버튼들
        #TotheMAP은 맵을 보여주기 위한 맵뷰
        self.TotheMAP.clicked.connect(self.MapView)
        #to_Start은 초기화면으로 돌아가기
        #self.to_Start.clicked.connect(self.reset_btn)


    def MapView(self):
        from test_api import show_html
        show_html()

    #def reset_btn(self):
    #    print("초기화 버튼이 클릭되었습니다.")


    #####
    #####
    #####
    #여기서 부터는 리스트를 띄우는 구간

    def deal(self):
        all_data = Attributes.GetResult(Attributes)
        self.km_dis.setText(str(Attributes.totalDistance)+"km")
        self.min_time.setText(Attributes.secToHour(Attributes.totalTime))



        def get_item_wight(data):
            #
            point_Name = data['point_Name']
            Num_Photo = data['Num_Photo']
            cumulative_Time = data['cumulative_Time']
            interval_Distance = data['interval_Distance']
            cumulative_Distance = data['cumulative_Distance']
            interval_Time = data['interval_Time']
            #  Widget
            wight = QWidget()
            #
            layout_main = QHBoxLayout() #큰틀 가로박스 레이아웃
            map_l = QLabel()  #이미지 크기
            map_l.setFixedSize(50, 50)
            maps = QPixmap(Num_Photo).scaled(50, 50)
            map_l.setPixmap(maps)
            #
            layout_right = QVBoxLayout() #오른쪽 세로박스 레이아웃
            #
            layout_right_down = QHBoxLayout()  #오른쪽 아래 가로박스 레이아웃
            layout_right_down.addWidget(QLabel("구간: "+interval_Distance+" km"))
            layout_right_down.addWidget(QLabel("누적: "+cumulative_Distance+" km"))
            layout_right_down.addWidget(QLabel("구간: "+interval_Time))
            layout_right_down.addWidget(QLabel("누적: "+cumulative_Time))
            #       ,
            layout_main.addWidget(map_l)  #
            layout_right.addWidget(QLabel(point_Name))  #
            layout_right.addLayout(layout_right_down)  #
            layout_main.addLayout(layout_right)  #
            wight.setLayout(layout_main)  # wight
            return wight  # wight

        for Dist_Data in all_data:
            item = QListWidgetItem()  # QListWidgetItem
            item.setSizeHint(QSize(200, 80))  # QListWidgetItem
            widget = get_item_wight(Dist_Data)  #
            self.listWidget.addItem(item)  # item
            self.listWidget.setItemWidget(item, widget)  # item  widget
