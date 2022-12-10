import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
        ,
    """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 380, 450))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 10, 100, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class Windows(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Windows, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.deal)

    def deal(self):
        all_data = json.loads(
            '[{"index_Num":"1","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/1.png"},{"index_Num":"2","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/2.png"},{"index_Num":"3","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/3.png"},{"index_Num":"4","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/4.png"},{"index_Num":"5","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/5.png"},{"index_Num":"6","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/6.png"},{"index_Num":"7","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/7.png"},{"index_Num":"8","point_Name":"주소","interval_Distance":"구간거리","cumulative_Distance":"누적거리","interval_Time":"구간시간","cumulative_Time":"누적시간","Num_Photo":"icon/8.png"}]'
        )

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
            map_l.setFixedSize(40, 25)
            maps = QPixmap(Num_Photo).scaled(40, 25)
            map_l.setPixmap(maps)
            #
            layout_right = QVBoxLayout() #오른쪽 세로박스 레이아웃
            #
            layout_right_down = QHBoxLayout()  #오른쪽 아래 가로박스 레이아웃
            layout_right_down.addWidget(QLabel(interval_Distance))
            layout_right_down.addWidget(QLabel(cumulative_Distance))
            layout_right_down.addWidget(QLabel(interval_Time))
            layout_right_down.addWidget(QLabel(cumulative_Time))
            #       ,
            layout_main.addWidget(map_l)  #
            layout_right.addWidget(QLabel(point_Name))  #
            layout_right.addLayout(layout_right_down)  #
            layout_main.addLayout(layout_right)  #
            wight.setLayout(layout_main)  # wight
            return wight  # wight

        for Dist_Data in all_data:
            item = QListWidgetItem()  # QListWidgetItem
            item.setSizeHint(QSize(200, 50))  # QListWidgetItem
            widget = get_item_wight(Dist_Data)  #
            self.listWidget.addItem(item)  # item
            self.listWidget.setItemWidget(item, widget)  # item  widget


app = QtWidgets.QApplication(sys.argv)
windows = Windows()
windows.show()
sys.exit(app.exec_())
