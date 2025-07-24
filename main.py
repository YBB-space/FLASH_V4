"""
⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠛⠻⣿⣿⠿⠛⠛⠙⠛⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⢀⣀⣀⡀⠀⠈⢄⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠏⠀⠀⠀⠔⠉⠁⠀⠀⠈⠉⠓⢼⡤⠔⠒⠀⠐⠒⠢⠌⠿⢿⣿⣿⣿⣿
⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢀⠤⣒⠶⠤⠭⠭⢝⡢⣄⢤⣄⣒⡶⠶⣶⣢⡝⢿⣿⣿
⡿⠋⠁⠀⠀⠀⠀⣀⠲⠮⢕⣽⠖⢩⠉⠙⣷⣶⣮⡍⢉⣴⠆⣭⢉⠑⣶⣮⣅⢻⣿
⠀⠀⠀⠀⠀⠀⠀⠉⠒⠒⠻⣿⣄⠤⠘⢃⣿⣿⡿⠫⣿⣿⣄⠤⠘⢃⣿⣿⠿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠤⠭⣥⣀⣉⡩⡥⠴⠃⠀⠈⠉⠁⠈⠉⠁⣴⣾⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠔⠊⠀⠀⠀⠓⠲⡤⠤⠖⠐⢿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢸⣿⡻⢷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣘⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠠⡀⠀⠙⢿⣷⣽⣽⣛⣟⣻⠷⠶⢶⣦⣤⣤⣤⣤⣶⠾⠟⣯⣿⣿
⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠶⠶⠶⠶⠾⣿⣟⣿⣿⣿
⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

HANWOOL
FCP Flash v4
© HANWOOL All Rights Reserved
2025 YBB(ybb1833@naver.com)
project site : https://github.com/YBB-space/FLASH_V4?tab=readme-ov-file#flash_v4
"""

import serial
import serial.tools.list_ports
from pathlib import Path
from PyQt5.QtTest import QTest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime
from PyQt5.QtGui import QColor
import os
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import time
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import sys
import os

#    자동으로 연결될 아두이노 장치를 필터링하는 키워드입니다.
#    사용 중인 기기에 따라 아래 변수를 수정하세요.
#    예시:
#      - "USB Serial" → CH340, 일부 Uno 계열
#      - "Arduino"     → 공식 Arduino 보드
#      - "ttyACM"      → 리눅스 환경, Uno 등
#      - "cu.usbmodem" → macOS 환경
DEVICE_KEYWORD = "USB Serial"  # ← 이 값을 수정하세요!!

# stdout 잠깐 비우기
sys_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
import pygame


port = ""
program_info_count = 0 # 프로그램 인포 버튼 클릭 확인
mode_count = 1 # 모드 변경 버튼 클릭 확인
mode_flight_count = 0 # 플라이트 모드 확인
mode_TMS_count = 0 # TMS 모드 확인
control_count = 0 # 컨트롤 버튼 클릭 확인
export_count = 0 # 익스포트 버튼 클릭 확인
terminal_count = 0 # 터미널 버튼 클릭 확인
safty_count = 0 # 세이프티 버튼 클릭 확인
chart_count = 0 # 차트 버튼 클릭 확인
set_count = 0 # 설정 버튼 클릭 확인
simulation_mode = 0 #시뮬레이션 모드 확인
abort = 0 #비행 중단 확인
t = 0 # 시퀀스 기본 시간
t_set = 0 # 시퀀스 선택 시간
sequence = 0 # 시퀀스 진행 확인
I_S = 5 # 수동 점화 = 0 , 시퀀스 시작 = 1 , 데이터 리셋 = 2 , 발사대 기립 = 3 , IFP_mode = 4 , Nomal = 5
intro_exit = 0 # 인트로 화면 확인
sim_ig = 0 # 시뮬레이션 모드 점화 확인
VFS_count = 1 #VFS 활성화 확인
ADI_count = 0 # ADI 활성화 확인
set_mode_count = 0
setting_interface_count = 1 #설정 1번 모드 확인

#여기 주석 다셈 ㅇㅇ 꼭!!!!!
IFP_confirm_popup_count = 0
simulation_data_count = 0
data_safe_count = 0
detail_log_count = 0
sequence_manual_ig__count = 0
IFP_count = 1
re_seq_count = 1

avg_parameter1_2 = 0
avg_parameter2_2 = 0
max_parameter1 = 0
max_parameter2 = 0

pygame.init()
pygame.mixer.init()

# stdout 복원
sys.stdout = sys_stdout

print("HANWOOL")
print("FCP Flash V4 macOS Edition")
print("© HANWOOL All Rights Reserved")
print("---------------------------------------------------")
print("기기 자동 연결 시도 중...")

# 1. 자동으로 아두이노 포트 찾기
arduino_ports = [
    p.device for p in serial.tools.list_ports.comports()
    if DEVICE_KEYWORD in p.description
]

if arduino_ports:
    # 자동 연결 성공
    port = arduino_ports[0]
    print(f"자동 연결 성공: {port}")
else:
    # 자동 연결 실패
    print("자동 연결 실패")
    
    # 2. 포트 목록 보여주기
    ports = list(serial.tools.list_ports.comports())
    
    if not ports:
        print("연결 가능한 포트가 없습니다. 연결 없이 진행합니다.")
    else:
        print("연결 가능한 포트 목록:")
        for i, p in enumerate(ports):
            print(f"{i+1}: {p.device} ({p.description})")

        # 3. 사용자에게 입력받기
        user_input = input("원하는 포트 번호를 입력해 주세요. ex) 1\n").strip().upper()
        
        if user_input == "S":
            print("시뮬레이션 모드로 작동합니다")
            simulation_mode = 1
        elif user_input == "s":
            print("시뮬레이션 모드로 작동합니다")
            simulation_mode = 1
        elif user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= len(ports):
                port = ports[num - 1].device
                try:
                    print(f"수동 연결 성공: {port}")
                except Exception as e:
                    print(f"연결 실패: {e}")
            else:
                print("잘못된 번호입니다. 시뮬레이션 모드로 작동합니다.")
                simulation_mode = 1
        else:
            print("잘못된 입력입니다. 시뮬레이션 모드로 작동합니다.")
            simulation_mode = 1

t_set = int(input("시퀀스 기본 시간을 입력해주세요. ex) 60\n"))


class SerialReaderThread(QThread):
    new_data_signal = pyqtSignal(str)  # 아두이노로부터 새 데이터를 받을 때 신호 발생

    def __init__(self, serial_connection):
        super().__init__()
        self.serial_connection = serial_connection
        self.is_running = True

    def run(self):
        while self.is_running:
            if intro_exit == 1:
                if self.serial_connection.in_waiting > 0:
                    serial_data = self.serial_connection.readline().decode(errors='ignore').strip()
                    self.new_data_signal.emit(serial_data)  # 새 데이터를 신호로 전송
            QTest.qWait(1)
        

class TimeUpdateThread(QObject):
    time_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.emit_time)

    def start(self):
        self.timer.start(1000)  # 1초 간격

    def stop(self):
        self.timer.stop()

    def emit_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_signal.emit(current_time)

class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()  # 클릭 시그널 정의

    def mousePressEvent(self, event):
        self.clicked.emit()  # 클릭되면 시그널 발생
        super().mousePressEvent(event)  # QLabel 기본 동작도 유지


class Ui_MainWindow(object):
    def __init__(self):
        self.ser = None

    def setupUi(self, MainWindow):

        
        global port
        #this
        if simulation_mode == 0:
            self.ser = serial.Serial(port, 19200)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1281, 721)
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Sequence_time_text = QtWidgets.QLabel(self.centralwidget)
        self.Sequence_time_text.setGeometry(QtCore.QRect(30, 50, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Advent Pro SemiExpanded")
        font.setPointSize(40)
        font.setBold(False) 
        font.setItalic(False)
        font.setWeight(50)



        self.safty_btn2 = ClickableLabel(self.centralwidget)
        self.safty_btn2.setGeometry(QtCore.QRect(230, 230, 20, 20))
        self.safty_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.safty_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.safty_btn2.setText("")
        safety_icon_img = Path(__file__).parent / "img" / "settings" / "safty_icon.png"
        self.safty_btn2.setPixmap(QtGui.QPixmap(str(safety_icon_img)))
        self.safty_btn2.setScaledContents(True)
        self.safty_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.safty_btn2.setObjectName("safty_btn2")
        self.set_btn_box = QtWidgets.QLabel(self.centralwidget)
        self.set_btn_box.setGeometry(QtCore.QRect(210, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.set_btn_box.setFont(font)
        self.set_btn_box.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.set_btn_box.setText("")
        self.set_btn_box.setAlignment(QtCore.Qt.AlignCenter)
        self.set_btn_box.setObjectName("set_btn_box")
        self.settings_box1 = QtWidgets.QLabel(self.centralwidget)
        self.settings_box1.setGeometry(QtCore.QRect(210, 0, 1091, 725))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_box1.setFont(font)
        self.settings_box1.setStyleSheet("background-color: rgb(0, 0, 0,230);")
        self.settings_box1.setText("")
        self.settings_box1.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_box1.setObjectName("settings_box1")
        self.Set_title = QtWidgets.QLabel(self.centralwidget)
        self.Set_title.setGeometry(QtCore.QRect(430, 50, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Set_title.setFont(font)
        self.Set_title.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font:  25pt \"Inter\";")
        self.Set_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Set_title.setObjectName("Set_title")
        self.set_desc = QtWidgets.QLabel(self.centralwidget)
        self.set_desc.setGeometry(QtCore.QRect(430, 80, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.set_desc.setFont(font)
        self.set_desc.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 12pt \"Inter\";")
        self.set_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.set_desc.setObjectName("set_desc")
        self.settings_exit_btn = ClickableLabel(self.centralwidget)
        self.settings_exit_btn.setGeometry(QtCore.QRect(230, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(25)
        self.settings_exit_btn.setFont(font)
        self.settings_exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_exit_btn.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font:200 14pt \"Inter\";")
        self.settings_exit_btn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_exit_btn.setObjectName("settings_exit_btn")
        
        self.settings_box2 = QtWidgets.QLabel(self.centralwidget)
        self.settings_box2.setGeometry(QtCore.QRect(210, 0, 181, 720))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_box2.setFont(font)
        self.settings_box2.setStyleSheet("background-color: rgb(20, 20, 20,159);")
        self.settings_box2.setText("")
        self.settings_box2.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_box2.setObjectName("settings_box2")
        self.settings_line = QtWidgets.QLabel(self.centralwidget)
        self.settings_line.setGeometry(QtCore.QRect(430, 120, 631, 1))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_line.setFont(font)
        self.settings_line.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.settings_line.setText("")
        self.settings_line.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_line.setObjectName("settings_box2")
        self.safty_btn1 = ClickableLabel(self.centralwidget)
        self.safty_btn1.setGeometry(QtCore.QRect(260, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.safty_btn1.setFont(font)
        self.safty_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.safty_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(172, 172, 172);\n"
"font: 400 12pt \"Inter\";")
        self.safty_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.safty_btn1.setObjectName("safty_btn1")
        self.sequence_btn1 = ClickableLabel(self.centralwidget)
        self.sequence_btn1.setGeometry(QtCore.QRect(260, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sequence_btn1.setFont(font)
        self.sequence_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sequence_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(172, 172, 172);\n"
"font: 400 12pt \"Inter\";")
        self.sequence_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sequence_btn1.setObjectName("sequence_btn1")
        self.advanced_btn1 = ClickableLabel(self.centralwidget)
        self.advanced_btn1.setGeometry(QtCore.QRect(260, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.advanced_btn1.setFont(font)
        self.advanced_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.advanced_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(172, 172, 172);\n"
"font: 400 12pt \"Inter\";")
        self.advanced_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.advanced_btn1.setObjectName("advanced_btn1")
        self.data_btn1 = ClickableLabel(self.centralwidget)
        self.data_btn1.setGeometry(QtCore.QRect(260, 150, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_btn1.setFont(font)
        self.data_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(172, 172, 172);\n"
"font: 400 12pt \"Inter\";")
        self.data_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.data_btn1.setObjectName("data_btn1")
        self.interface_btn1 = ClickableLabel(self.centralwidget)
        self.interface_btn1.setGeometry(QtCore.QRect(260, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.interface_btn1.setFont(font)
        self.interface_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.interface_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(172, 172, 172);\n"
"font: 400 12pt \"Inter\";")
        self.interface_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.interface_btn1.setObjectName("interface_btn1")
        self.sequence_btn2 = ClickableLabel(self.centralwidget)
        self.sequence_btn2.setGeometry(QtCore.QRect(230, 190, 20, 20))
        self.sequence_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sequence_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.sequence_btn2.setText("")
        sequence_icon_img = Path(__file__).parent / "img" / "settings" / "sequence_icon.png"
        self.sequence_btn2.setPixmap(QtGui.QPixmap(str(sequence_icon_img)))
        self.sequence_btn2.setScaledContents(True)
        self.sequence_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.sequence_btn2.setObjectName("sequence_btn2")
        self.data_btn2 = ClickableLabel(self.centralwidget)
        self.data_btn2.setGeometry(QtCore.QRect(230, 150, 20, 20))
        self.data_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.data_btn2.setText("")
        data_icon_img = Path(__file__).parent / "img" / "settings" / "data_icon.png"
        self.data_btn2.setPixmap(QtGui.QPixmap(str(data_icon_img)))
        self.data_btn2.setScaledContents(True)
        self.data_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.data_btn2.setObjectName("data_btn2")
        self.advanced_btn2 = ClickableLabel(self.centralwidget)
        self.advanced_btn2.setGeometry(QtCore.QRect(230, 110, 20, 20))
        self.advanced_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.advanced_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.advanced_btn2.setText("")
        advanced_icon_img = Path(__file__).parent / "img" / "settings" / "advanced_icon.png"
        self.advanced_btn2.setPixmap(QtGui.QPixmap(str(advanced_icon_img)))
        self.advanced_btn2.setScaledContents(True)
        self.advanced_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.advanced_btn2.setObjectName("advanced_btn2")
        self.interface_btn2 = ClickableLabel(self.centralwidget)
        self.interface_btn2.setGeometry(QtCore.QRect(230, 70, 20, 20))
        self.interface_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.interface_btn2.setText("")
        interface_icon_img = Path(__file__).parent / "img" / "settings" / "interface_icon.png"
        self.interface_btn2.setPixmap(QtGui.QPixmap(str(interface_icon_img)))
        self.interface_btn2.setScaledContents(True)
        self.interface_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.interface_btn2.setObjectName("interface_btn2")
        self.settings_text1_1 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text1_1.setGeometry(QtCore.QRect(430, 140, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_text1_1.setFont(font)
        self.settings_text1_1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 400 15pt \"Inter\";\n"
"color: rgb(208, 208, 208);")
        self.settings_text1_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text1_1.setObjectName("settings_text1_1")
        self.settings_text1_2 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text1_2.setGeometry(QtCore.QRect(430, 160, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.settings_text1_2.setFont(font)
        self.settings_text1_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Inter\";")
        self.settings_text1_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text1_2.setObjectName("settings_text1_2")
        self.set_interface2_img_box = QtWidgets.QLabel(self.centralwidget)
        self.set_interface2_img_box.setGeometry(QtCore.QRect(430, 312, 391, 131))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.set_interface2_img_box.setFont(font)
        self.set_interface2_img_box.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(31, 31, 31);")
        self.set_interface2_img_box.setText("")
        self.set_interface2_img_box.setAlignment(QtCore.Qt.AlignCenter)
        self.set_interface2_img_box.setObjectName("set_interface2_img_box")
        self.settings_text2_2 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text2_2.setGeometry(QtCore.QRect(430, 250, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.settings_text2_2.setFont(font)
        self.settings_text2_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Inter\";")
        self.settings_text2_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text2_2.setObjectName("settings_text2_2")
        self.settings_text2_1 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text2_1.setGeometry(QtCore.QRect(430, 230, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_text2_1.setFont(font)
        self.settings_text2_1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 400 15pt \"Inter\";\n"
"color: rgb(208, 208, 208);")
        self.settings_text2_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text2_1.setObjectName("settings_text2_1")
        self.settings_btn1_1 = ClickableLabel(self.centralwidget)
        self.settings_btn1_1.setGeometry(QtCore.QRect(430, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_btn1_1.setFont(font)
        self.settings_btn1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
        self.settings_btn1_1.setText("")
        self.settings_btn1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_btn1_1.setObjectName("settings_btn1_1")

        
        self.settings_btn1_2 = ClickableLabel(self.centralwidget)
        self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_btn1_2.setFont(font)
        self.settings_btn1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn1_2.setStyleSheet("border-radius :8px;\n"
"background-color: rgb(255, 255, 255);")
        self.settings_btn1_2.setText("")
        self.settings_btn1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_btn1_2.setObjectName("settings_btn1_2")
        self.settings_btn1_3 = ClickableLabel(self.centralwidget)
        self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_btn1_3.setFont(font)
        self.settings_btn1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn1_3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 400 8pt \"Inter\";")
        self.settings_btn1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_btn1_3.setObjectName("settings_btn1_3")
        self.set_a_btn3 = ClickableLabel(self.centralwidget)
        self.set_a_btn3.setGeometry(QtCore.QRect(1129, 102, 20, 17))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.set_a_btn3.setFont(font)
        self.set_a_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_a_btn3.setStyleSheet("border-radius :8px;\n"
"background-color: rgb(255, 255, 255);")
        self.set_a_btn3.setText("")
        self.set_a_btn3.setAlignment(QtCore.Qt.AlignCenter)
        self.set_a_btn3.setObjectName("set_a_btn3")
        self.set_a_btn2 = ClickableLabel(self.centralwidget)
        self.set_a_btn2.setGeometry(QtCore.QRect(650, 530, 51, 21))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.set_a_btn2.setFont(font)
        self.set_a_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_a_btn2.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(50,205,50);")
        self.set_a_btn2.setText("")
        self.set_a_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.set_a_btn2.setObjectName("set_a_btn2")
        self.set_a_btn3_2 = ClickableLabel(self.centralwidget)
        self.set_a_btn3_2.setGeometry(QtCore.QRect(660, 530, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.set_a_btn3_2.setFont(font)
        self.set_a_btn3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_a_btn3_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 400 10pt \"Inter\";")
        self.set_a_btn3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.set_a_btn3_2.setObjectName("set_a_btn3_2")
        self.set_interface2_img = QtWidgets.QLabel(self.centralwidget)
        self.set_interface2_img.setGeometry(QtCore.QRect(435, 317, 381, 121))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.set_interface2_img.setFont(font)
        self.set_interface2_img.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(31, 31, 31);")
        self.set_interface2_img.setText("")
        set_interface2_img = Path(__file__).parent / "img" / "settings" / "ADI_img.png"
        self.set_interface2_img.setPixmap(QtGui.QPixmap(str(set_interface2_img)))
        self.set_interface2_img.setScaledContents(True)
        self.set_interface2_img.setAlignment(QtCore.Qt.AlignCenter)
        self.set_interface2_img.setWordWrap(False)
        self.set_interface2_img.setOpenExternalLinks(False)
        self.set_interface2_img.setObjectName("set_interface2_img")
        self.settings_text2_3 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text2_3.setGeometry(QtCore.QRect(430, 442, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.settings_text2_3.setFont(font)
        self.settings_text2_3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 8pt \"Inter\";")
        self.settings_text2_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text2_3.setObjectName("settings_text2_3")
        self.settings_btn2_1 = ClickableLabel(self.centralwidget)
        self.settings_btn2_1.setGeometry(QtCore.QRect(430, 280, 51, 21))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_btn2_1.setFont(font)
        self.settings_btn2_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn2_1.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(50,205,50);")
        self.settings_btn2_1.setText("")
        self.settings_btn2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_btn2_1.setObjectName("settings_btn2_1")
        self.settings_btn2_3 = ClickableLabel(self.centralwidget)
        self.settings_btn2_3.setGeometry(QtCore.QRect(459, 282, 20, 17))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.settings_btn2_3.setFont(font)
        self.settings_btn2_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn2_3.setStyleSheet("border-radius :8px;\n"
"background-color: rgb(255, 255, 255);")
        self.settings_btn2_3.setText("")
        self.settings_btn2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_btn2_3.setObjectName("settings_btn2_3")
        self.settings_btn2_2 = ClickableLabel(self.centralwidget)
        self.settings_btn2_2.setGeometry(QtCore.QRect(430, 280, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_btn2_2.setFont(font)
        self.settings_btn2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn2_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 400 8pt \"Inter\";")
        self.settings_btn2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_btn2_2.setObjectName("settings_btn2_2")
        self.programinfo_btn1 = ClickableLabel(self.centralwidget)
        self.programinfo_btn1.setGeometry(QtCore.QRect(260, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.programinfo_btn1.setFont(font)
        self.programinfo_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.programinfo_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(172, 172, 172);\n"
"font: 400 12pt \"Inter\";")
        self.programinfo_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.programinfo_btn1.setObjectName("programinfo_btn1")
        self.programinfo_btn2 = ClickableLabel(self.centralwidget)
        self.programinfo_btn2.setGeometry(QtCore.QRect(230, 270, 20, 20))
        self.programinfo_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.programinfo_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.programinfo_btn2.setText("")
        programinfo_icon_img = Path(__file__).parent / "img" / "settings" / "information_icon.png"
        self.programinfo_btn2.setPixmap(QtGui.QPixmap(str(programinfo_icon_img)))
        self.programinfo_btn2.setScaledContents(True)
        self.programinfo_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.programinfo_btn2.setObjectName("programinfo_btn2")
        self.settings_text3_2 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text3_2.setGeometry(QtCore.QRect(430, 500, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.settings_text3_2.setFont(font)
        self.settings_text3_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Inter\";")
        self.settings_text3_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text3_2.setObjectName("settings_text3_2")
        self.settings_text3_1 = QtWidgets.QLabel(self.centralwidget)
        self.settings_text3_1.setGeometry(QtCore.QRect(430, 480, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_text3_1.setFont(font)
        self.settings_text3_1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 400 15pt \"Inter\";\n"
"color: rgb(208, 208, 208);")
        self.settings_text3_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_text3_1.setObjectName("settings_text3_1")
        self.set_interface3_Cbtn1 = QtWidgets.QCheckBox(self.centralwidget)
        self.set_interface3_Cbtn1.setGeometry(QtCore.QRect(430, 530, 71, 20))
        self.set_interface3_Cbtn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_interface3_Cbtn1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 300 10pt \"Inter\";")
        self.set_interface3_Cbtn1.setChecked(False)
        self.set_interface3_Cbtn1.setAutoRepeat(False)
        self.set_interface3_Cbtn1.setTristate(False)
        self.set_interface3_Cbtn1.setObjectName("set_interface3_Cbtn1")
        self.set_interface3_Cbtn2 = QtWidgets.QCheckBox(self.centralwidget)
        self.set_interface3_Cbtn2.setGeometry(QtCore.QRect(510, 530, 51, 20))
        self.set_interface3_Cbtn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_interface3_Cbtn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 300 10pt \"Inter\";")
        self.set_interface3_Cbtn2.setChecked(False)
        self.set_interface3_Cbtn2.setAutoRepeat(False)
        self.set_interface3_Cbtn2.setTristate(False)
        self.set_interface3_Cbtn2.setObjectName("set_interface3_Cbtn2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(850, 720, 87, 20))
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 300 10pt \"Inter\";")
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setAutoRepeat(False)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.set_interface3_Cbtn3 = QtWidgets.QCheckBox(self.centralwidget)
        self.set_interface3_Cbtn3.setGeometry(QtCore.QRect(580, 530, 51, 20))
        self.set_interface3_Cbtn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_interface3_Cbtn3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 300 10pt \"Inter\";")
        self.set_interface3_Cbtn3.setChecked(False)
        self.set_interface3_Cbtn3.setAutoRepeat(False)
        self.set_interface3_Cbtn3.setTristate(False)
        self.set_interface3_Cbtn3.setObjectName("set_interface3_Cbtn3")
        self.set_a_spinbox1 = QtWidgets.QLabel(self.centralwidget)
        self.set_a_spinbox1.setGeometry(QtCore.QRect(1100, 135, 51, 31))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.set_a_spinbox1.setFont(font)
        self.set_a_spinbox1.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(31, 31, 31);")
        self.set_a_spinbox1.setText("")
        self.set_a_spinbox1.setAlignment(QtCore.Qt.AlignCenter)
        self.set_a_spinbox1.setObjectName("set_a_spinbox1")
        self.set_a_spin1 = QtWidgets.QSpinBox(self.centralwidget)
        self.set_a_spin1.setGeometry(QtCore.QRect(1107, 140, 41, 21))
        self.set_a_spin1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Inter\";")
        self.set_a_spin1.setObjectName("set_a_spin1")


        self.Sequence_time_text.setFont(font)
        self.Sequence_time_text.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 40pt \"Advent Pro SemiExpanded\";")
        self.Sequence_time_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Sequence_time_text.setObjectName("Sequence_time_text")
        self.parameter1_box = QtWidgets.QLabel(self.centralwidget)
        self.parameter1_box.setGeometry(QtCore.QRect(940, 540, 150, 150))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parameter1_box.setFont(font)
        self.parameter1_box.setStyleSheet("border-radius :75px;\n"
"font: 20pt \"AppleSDGothicNeoSB00\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 25, 25, 150), stop:1 rgba(81, 81, 81, 100));")
        self.parameter1_box.setText("")
        self.parameter1_box.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter1_box.setObjectName("parameter1_box")
        

        self.gauge_r = QtWidgets.QLabel(self.centralwidget)
        self.gauge_r.setGeometry(QtCore.QRect(930, 520, 170, 170))
        self.gauge_r.setFont(font)
        self.gauge_r.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n")
        self.gauge_r.setText("")
        gauge_r_img = Path(__file__).parent / "img" / "gauge" / "Gauge_R_01.png"
        self.gauge_r.setPixmap(QtGui.QPixmap(str(gauge_r_img)))
        self.gauge_r.setScaledContents(True)
        self.gauge_r.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gauge_r.setObjectName("gauge_r_img")

        self.gauge_b = QtWidgets.QLabel(self.centralwidget)
        self.gauge_b.setGeometry(QtCore.QRect(1090, 520, 170, 170))
        self.gauge_b.setFont(font)
        self.gauge_b.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n")
        self.gauge_b.setText("")
        gauge_b_img = Path(__file__).parent / "img" / "gauge" / "Gauge_B_01.png"
        self.gauge_b.setPixmap(QtGui.QPixmap(str(gauge_b_img)))
        self.gauge_b.setScaledContents(True)
        self.gauge_b.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gauge_b.setObjectName("gauge_b_img")


        self.parameter1_text2 = QtWidgets.QLabel(self.centralwidget)
        self.parameter1_text2.setGeometry(QtCore.QRect(1000, 640, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parameter1_text2.setFont(font)
        self.parameter1_text2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"font: 63 11pt \"Inter\";\n"
"color: rgb(255, 255, 255);")
        self.parameter1_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter1_text2.setObjectName("parameter1_text2")
        self.parameter1_text1 = QtWidgets.QLabel(self.centralwidget)
        self.parameter1_text1.setGeometry(QtCore.QRect(980, 580, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.parameter1_text1.setFont(font)
        self.parameter1_text1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Inter\";")
        self.parameter1_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter1_text1.setObjectName("parameter1_text1")
        self.Flight_interface_Box = QtWidgets.QLabel(self.centralwidget)
        self.Flight_interface_Box.setGeometry(QtCore.QRect(20, 635, 571, 51))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Flight_interface_Box.setFont(font)
        self.Flight_interface_Box.setStyleSheet("border-radius :13px;\n"
"background-color: rgb(0, 0, 0);")
        self.Flight_interface_Box.setText("")
        self.Flight_interface_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_Box.setObjectName("Flight_interface_Box")
        self.parameter1_main = QtWidgets.QLabel(self.centralwidget)
        self.parameter1_main.setGeometry(QtCore.QRect(960, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parameter1_main.setFont(font)
        self.parameter1_main.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Inter\";")
        self.parameter1_main.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter1_main.setObjectName("parameter1_main")
        self.back_grad_up = QtWidgets.QLabel(self.centralwidget)
        self.back_grad_up.setGeometry(QtCore.QRect(0, -10, 1281, 211))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.back_grad_up.setFont(font)
        self.back_grad_up.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 200), stop:1 rgba(255, 255, 255, 0));")
        self.back_grad_up.setText("")
        self.back_grad_up.setAlignment(QtCore.Qt.AlignCenter)
        self.back_grad_up.setObjectName("back_grad_up")
        self.Abort_text = QtWidgets.QLabel(self.centralwidget)
        self.Abort_text.setGeometry(QtCore.QRect(730, 640, 201, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Abort_text.setFont(font)
        self.Abort_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 9pt \"AppleSDGothicNeoUL00\";")
        self.Abort_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Abort_text.setObjectName("Abort_text")
        self.flight_info_text = QtWidgets.QLabel(self.centralwidget)
        self.flight_info_text.setGeometry(QtCore.QRect(30, 100, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.flight_info_text.setFont(font)
        self.flight_info_text.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 20pt \"Inter\";")
        self.flight_info_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.flight_info_text.setObjectName("flight_info_text")
        self.flight_data_text = QtWidgets.QLabel(self.centralwidget)
        self.flight_data_text.setGeometry(QtCore.QRect(30, 130, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.flight_data_text.setFont(font)
        self.flight_data_text.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 57 13pt \"Inter\";")
        self.flight_data_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.flight_data_text.setObjectName("flight_data_text")
        self.back_grad_down = QtWidgets.QLabel(self.centralwidget)
        self.back_grad_down.setGeometry(QtCore.QRect(0, 590, 1281, 131))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.back_grad_down.setFont(font)
        self.back_grad_down.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(0, 0, 0, 150));")
        self.back_grad_down.setText("")
        self.back_grad_down.setAlignment(QtCore.Qt.AlignCenter)
        self.back_grad_down.setObjectName("back_grad_down")
        self.Flight_interface_Mode_btn1 = ClickableLabel(self.centralwidget)
        self.Flight_interface_Mode_btn1.setGeometry(QtCore.QRect(25, 640, 151, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Flight_interface_Mode_btn1.setFont(font)
        self.Flight_interface_Mode_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_Mode_btn1.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(25, 25, 25);")
        self.Flight_interface_Mode_btn1.setText("")
        self.Flight_interface_Mode_btn1.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_Mode_btn1.setObjectName("Flight_interface_Mode_btn1")
        self.Flight_interface_Mode_btn2 = ClickableLabel(self.centralwidget)
        self.Flight_interface_Mode_btn2.setGeometry(QtCore.QRect(70, 647, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter 18pt")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Flight_interface_Mode_btn2.setFont(font)
        self.Flight_interface_Mode_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_Mode_btn2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Inter 18pt\";")
        self.Flight_interface_Mode_btn2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Flight_interface_Mode_btn2.setObjectName("Flight_interface_Mode_btn2")
        self.Flight_interface_Mode_btn3 = ClickableLabel(self.centralwidget)
        self.Flight_interface_Mode_btn3.setGeometry(QtCore.QRect(70, 661, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Flight_interface_Mode_btn3.setFont(font)
        self.Flight_interface_Mode_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_Mode_btn3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 8pt \"Inter\";")
        self.Flight_interface_Mode_btn3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Flight_interface_Mode_btn3.setObjectName("Flight_interface_Mode_btn3")
        self.Flight_interface_Time = QtWidgets.QLabel(self.centralwidget)
        self.Flight_interface_Time.setGeometry(QtCore.QRect(500, 650, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 18pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Flight_interface_Time.setFont(font)
        self.Flight_interface_Time.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(167, 167, 167);\n"
"font: 15pt \"Inter 18pt\";")
        self.Flight_interface_Time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Flight_interface_Time.setObjectName("Flight_interface_Time")
        self.Flight_interface_Control_btn = ClickableLabel(self.centralwidget)
        self.Flight_interface_Control_btn.setGeometry(QtCore.QRect(210, 650, 21, 21))
        self.Flight_interface_Control_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_Control_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_Control_btn.setText("")
        control_img_path = Path(__file__).parent / "img" / "control.png"
        self.Flight_interface_Control_btn.setPixmap(QtGui.QPixmap(str(control_img_path)))
        self.Flight_interface_Control_btn.setScaledContents(True)
        self.Flight_interface_Control_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_Control_btn.setObjectName("Flight_interface_Control_btn")
        self.Flight_interface_export_btn = ClickableLabel(self.centralwidget)
        self.Flight_interface_export_btn.setGeometry(QtCore.QRect(271, 650, 19, 21))
        self.Flight_interface_export_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_export_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_export_btn.setText("")
        export_img_path = Path(__file__).parent / "img" / "export.png"
        self.Flight_interface_export_btn.setPixmap(QtGui.QPixmap(str(export_img_path)))
        self.Flight_interface_export_btn.setScaledContents(True)
        self.Flight_interface_export_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_export_btn.setObjectName("Flight_interface_export_btn")
        self.Flight_interface_chart_btn = ClickableLabel(self.centralwidget)
        self.Flight_interface_chart_btn.setGeometry(QtCore.QRect(330, 650, 21, 21))
        self.Flight_interface_chart_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_chart_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_chart_btn.setText("")
        chart_img_path = Path(__file__).parent / "img" / "chart.png"
        self.Flight_interface_chart_btn.setPixmap(QtGui.QPixmap(str(chart_img_path)))
        self.Flight_interface_chart_btn.setScaledContents(True)
        self.Flight_interface_chart_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_chart_btn.setObjectName("Flight_interface_chart_btn")
        self.Flight_interface_seting_btn = ClickableLabel(self.centralwidget)
        self.Flight_interface_seting_btn.setGeometry(QtCore.QRect(450, 650, 21, 21))
        self.Flight_interface_seting_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_seting_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_seting_btn.setText("")
        setting_img_path = Path(__file__).parent / "img" / "setting.png"
        self.Flight_interface_seting_btn.setPixmap(QtGui.QPixmap(str(setting_img_path)))
        self.Flight_interface_seting_btn.setScaledContents(True)
        self.Flight_interface_seting_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_seting_btn.setObjectName("Flight_interface_seting_btn")
        self.Flight_interface_line4 = QtWidgets.QLabel(self.centralwidget)
        self.Flight_interface_line4.setGeometry(QtCore.QRect(430, 650, 1, 25))
        self.Flight_interface_line4.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.Flight_interface_line4.setText("")
        self.Flight_interface_line4.setObjectName("Flight_interface_line4")
        self.Flight_interface_line2 = QtWidgets.QLabel(self.centralwidget)
        self.Flight_interface_line2.setGeometry(QtCore.QRect(310, 650, 1, 25))
        self.Flight_interface_line2.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.Flight_interface_line2.setText("")
        self.Flight_interface_line2.setObjectName("Flight_interface_line2")
        self.Flight_interface_line3 = QtWidgets.QLabel(self.centralwidget)
        self.Flight_interface_line3.setGeometry(QtCore.QRect(370, 650, 1, 25))
        self.Flight_interface_line3.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.Flight_interface_line3.setText("")
        self.Flight_interface_line3.setObjectName("Flight_interface_line3")
        self.Flight_interface_line1 = QtWidgets.QLabel(self.centralwidget)
        self.Flight_interface_line1.setGeometry(QtCore.QRect(250, 650, 1, 25))
        self.Flight_interface_line1.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.Flight_interface_line1.setText("")
        self.Flight_interface_line1.setObjectName("Flight_interface_line1")
        self.Flight_interface_Mode_btn4 = ClickableLabel(self.centralwidget)
        self.Flight_interface_Mode_btn4.setGeometry(QtCore.QRect(34, 649, 25, 25))
        self.Flight_interface_Mode_btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_Mode_btn4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_Mode_btn4.setText("")
        TMS_img_path = Path(__file__).parent / "img" / "TMS.png"
        self.Flight_interface_Mode_btn4.setPixmap(QtGui.QPixmap(str(TMS_img_path)))
        self.Flight_interface_Mode_btn4.setScaledContents(True)
        self.Flight_interface_Mode_btn4.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_Mode_btn4.setObjectName("Flight_interface_Mode_btn4")
        self.Flight_interface_ModeUP_btn5 = ClickableLabel(self.centralwidget)
        self.Flight_interface_ModeUP_btn5.setGeometry(QtCore.QRect(154, 657, 10, 6))
        self.Flight_interface_ModeUP_btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_ModeUP_btn5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_ModeUP_btn5.setText("")
        mode_DN_img_path = Path(__file__).parent / "img" / "mode_down.png"
        self.Flight_interface_ModeUP_btn5.setPixmap(QtGui.QPixmap(str(mode_DN_img_path)))
        self.Flight_interface_ModeUP_btn5.setScaledContents(True)
        self.Flight_interface_ModeUP_btn5.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_ModeUP_btn5.setObjectName("Flight_interface_ModeUP_btn5")
        self.Control_box = QtWidgets.QLabel(self.centralwidget)
        self.Control_box.setGeometry(QtCore.QRect(24, 529, 561, 93))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Control_box.setFont(font)
        self.Control_box.setStyleSheet("border-radius :13px;\n"
"background-color: rgb(0, 0, 0);")
        self.Control_box.setText("")
        self.Control_box.setAlignment(QtCore.Qt.AlignCenter)
        self.Control_box.setObjectName("Control_box")
        self.Control_HWCheck_btn2 = ClickableLabel(self.centralwidget)
        self.Control_HWCheck_btn2.setGeometry(QtCore.QRect(125, 590, 2, 15))
        self.Control_HWCheck_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_HWCheck_btn2.setStyleSheet("border-radius :1px;\n"
"background-color: rgb(43, 162, 255);")
        self.Control_HWCheck_btn2.setText("")
        self.Control_HWCheck_btn2.setObjectName("Control_HWCheck_btn2")
        self.Control_HWCheck_btn4 = ClickableLabel(self.centralwidget)
        self.Control_HWCheck_btn4.setGeometry(QtCore.QRect(115, 535, 81, 81))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Control_HWCheck_btn4.setFont(font)
        self.Control_HWCheck_btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_HWCheck_btn4.setStyleSheet("border-radius :9px;\n"
"background-color: rgb(54, 159, 255,60);")
        self.Control_HWCheck_btn4.setText("")
        self.Control_HWCheck_btn4.setAlignment(QtCore.Qt.AlignCenter)
        self.Control_HWCheck_btn4.setObjectName("Control_HWCheck_btn4")
        self.Control_HWCheck_btn3 = ClickableLabel(self.centralwidget)
        self.Control_HWCheck_btn3.setGeometry(QtCore.QRect(145, 585, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 24pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Control_HWCheck_btn3.setFont(font)
        self.Control_HWCheck_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_HWCheck_btn3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 15pt \"Inter 24pt\";\n"
"color: rgb(28, 115, 255);")
        self.Control_HWCheck_btn3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Control_HWCheck_btn3.setObjectName("Control_HWCheck_btn3")
        self.Control_1ignition_btn1 = ClickableLabel(self.centralwidget)
        self.Control_1ignition_btn1.setGeometry(QtCore.QRect(210, 540, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Control_1ignition_btn1.setFont(font)
        self.Control_1ignition_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_1ignition_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 10pt \"Inter\";\n"
"color: rgb(183, 142, 142);")
        self.Control_1ignition_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Control_1ignition_btn1.setObjectName("Control_1ignition_btn1")
        self.Control_1ignition_btn2 = ClickableLabel(self.centralwidget)
        self.Control_1ignition_btn2.setGeometry(QtCore.QRect(200, 535, 81, 81))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Control_1ignition_btn2.setFont(font)
        self.Control_1ignition_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_1ignition_btn2.setStyleSheet("border-radius :9px;\n"
"background-color: rgb(255, 54, 54,60);")
        self.Control_1ignition_btn2.setText("")
        self.Control_1ignition_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.Control_1ignition_btn2.setObjectName("Control_1ignition_btn2")
        self.Control_1ignition_btn4 = ClickableLabel(self.centralwidget)
        self.Control_1ignition_btn4.setGeometry(QtCore.QRect(230, 585, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 24pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Control_1ignition_btn4.setFont(font)
        self.Control_1ignition_btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_1ignition_btn4.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 15pt \"Inter 24pt\";\n"
"color: rgb(211, 35, 0);")
        
        self.Control_1ignition_btn4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Control_1ignition_btn4.setObjectName("Control_1ignition_btn4")
        self.Control_1ignition_btn3 = ClickableLabel(self.centralwidget)
        self.Control_1ignition_btn3.setGeometry(QtCore.QRect(210, 590, 2, 15))
        self.Control_1ignition_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_1ignition_btn3.setStyleSheet("border-radius :1px;\n"
"background-color: rgb(211, 35, 0);")
        self.Control_1ignition_btn3.setText("")
        self.Control_1ignition_btn3.setObjectName("Control_1ignition_btn3")
        self.Control_HWCheck_btn1 = ClickableLabel(self.centralwidget)
        self.Control_HWCheck_btn1.setGeometry(QtCore.QRect(125, 540, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Control_HWCheck_btn1.setFont(font)
        self.Control_HWCheck_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_HWCheck_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(145, 201, 255);\n"
"font: 25 10pt \"Inter\";")
        self.Control_HWCheck_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Control_HWCheck_btn1.setObjectName("Control_HWCheck_btn1")
        self.Program_Info_btn = ClickableLabel(self.centralwidget)
        self.Program_Info_btn.setGeometry(QtCore.QRect(1210, 22, 51, 51))
        self.Program_Info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Program_Info_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Program_Info_btn.setText("")
        logo_img_path = Path(__file__).parent / "img" / "Flash_logo.png"
        self.Program_Info_btn.setPixmap(QtGui.QPixmap(str(logo_img_path)))
        self.Program_Info_btn.setScaledContents(True)
        self.Program_Info_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Program_Info_btn.setObjectName("Program_Info_btn")
        
        self.step = QtWidgets.QLabel(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(305, 580, 250, 34))
        self.step.setFont(font)
        self.step.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n")
        self.step.setText("")
        step_img = Path(__file__).parent / "img" / "step" / "step_1_1.png"
        self.step.setPixmap(QtGui.QPixmap(str(step_img)))
        self.step.setScaledContents(True)
        self.step.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.step.setObjectName("step")

        self.data_reset_btn = ClickableLabel(self.centralwidget)
        self.data_reset_btn.setGeometry(QtCore.QRect(287, 540, 70, 30))
        self.data_reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_reset_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.data_reset_btn.setText("")
        logo_img_path = Path(__file__).parent / "img" / "data_reset_btn.png"
        self.data_reset_btn.setPixmap(QtGui.QPixmap(str(logo_img_path)))
        self.data_reset_btn.setScaledContents(True)
        self.data_reset_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.data_reset_btn.setObjectName("data_reset_btn")

        self.seq_t_plus10_btn = ClickableLabel(self.centralwidget)
        self.seq_t_plus10_btn.setGeometry(QtCore.QRect(360, 540, 70, 30))
        self.seq_t_plus10_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seq_t_plus10_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.seq_t_plus10_btn.setText("")
        logo_img_path = Path(__file__).parent / "img" / "seq_t+10_btn.png"
        self.seq_t_plus10_btn.setPixmap(QtGui.QPixmap(str(logo_img_path)))
        self.seq_t_plus10_btn.setScaledContents(True)
        self.seq_t_plus10_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.seq_t_plus10_btn.setObjectName("seq_t_plus10_btn")

        self.seq_t_minus10_btn = ClickableLabel(self.centralwidget)
        self.seq_t_minus10_btn.setGeometry(QtCore.QRect(433, 540, 70, 30))
        self.seq_t_minus10_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seq_t_minus10_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.seq_t_minus10_btn.setText("")
        logo_img_path = Path(__file__).parent / "img" / "seq_t-10_btn.png"
        self.seq_t_minus10_btn.setPixmap(QtGui.QPixmap(str(logo_img_path)))
        self.seq_t_minus10_btn.setScaledContents(True)
        self.seq_t_minus10_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.seq_t_minus10_btn.setObjectName("seq_t_minus10_btn")

        self.re_seq_btn = ClickableLabel(self.centralwidget)
        self.re_seq_btn.setGeometry(QtCore.QRect(506, 540, 70, 30))
        self.re_seq_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.re_seq_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.re_seq_btn.setText("")
        logo_img_path = Path(__file__).parent / "img" / "re_seq_btn.png"
        self.re_seq_btn.setPixmap(QtGui.QPixmap(str(logo_img_path)))
        self.re_seq_btn.setScaledContents(True)
        self.re_seq_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.re_seq_btn.setObjectName("re_seq_btn")

        self.parameter2_text1 = QtWidgets.QLabel(self.centralwidget)
        self.parameter2_text1.setGeometry(QtCore.QRect(1140, 580, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.parameter2_text1.setFont(font)
        self.parameter2_text1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Inter\";")
        self.parameter2_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter2_text1.setObjectName("parameter2_text1")
        self.parameter2_text2 = QtWidgets.QLabel(self.centralwidget)
        self.parameter2_text2.setGeometry(QtCore.QRect(1160, 640, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parameter2_text2.setFont(font)
        self.parameter2_text2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"font: 63 11pt \"Inter\";\n"
"color: rgb(255, 255, 255);")
        self.parameter2_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter2_text2.setObjectName("parameter2_text2")
        self.parameter2_box = QtWidgets.QLabel(self.centralwidget)
        self.parameter2_box.setGeometry(QtCore.QRect(1100, 540, 150, 150))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parameter2_box.setFont(font)
        self.parameter2_box.setStyleSheet("border-radius :75px;\n"
"font: 20pt \"AppleSDGothicNeoSB00\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 25, 25, 150), stop:1 rgba(81, 81, 81, 100));")
        self.parameter2_box.setText("")
        self.parameter2_box.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter2_box.setObjectName("parameter2_box")
        self.parameter2_main = QtWidgets.QLabel(self.centralwidget)
        self.parameter2_main.setGeometry(QtCore.QRect(1120, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parameter2_main.setFont(font)
        self.parameter2_main.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Inter\";")
        self.parameter2_main.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter2_main.setObjectName("parameter2_main")
        self.Abort_btn2 = ClickableLabel(self.centralwidget)
        self.Abort_btn2.setGeometry(QtCore.QRect(599, 640, 121, 42))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Abort_btn2.setFont(font)
        self.Abort_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Abort_btn2.setStyleSheet("border-radius :9px;\n"
"background-color: rgb(255, 54, 54,60);")
        self.Abort_btn2.setText("")
        self.Abort_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.Abort_btn2.setObjectName("Abort_btn2")
        self.Abort_btn1 = ClickableLabel(self.centralwidget)
        self.Abort_btn1.setGeometry(QtCore.QRect(630, 650, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Inter 24pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Abort_btn1.setFont(font)
        self.Abort_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Abort_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 15pt \"Inter 24pt\";\n"
"color: rgb(211, 35, 0);")
        self.Abort_btn1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Abort_btn1.setObjectName("Abort_btn1")
        self.Abort_Box = QtWidgets.QLabel(self.centralwidget)
        self.Abort_Box.setGeometry(QtCore.QRect(594, 635, 131, 51))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Abort_Box.setFont(font)
        self.Abort_Box.setStyleSheet("border-radius :13px;\n"
"background-color: rgb(0, 0, 0);")
        self.Abort_Box.setText("")
        self.Abort_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Abort_Box.setObjectName("Abort_Box")
        self.Abort_btn3 = ClickableLabel(self.centralwidget)
        self.Abort_btn3.setGeometry(QtCore.QRect(620, 653, 2, 15))
        self.Abort_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Abort_btn3.setStyleSheet("border-radius :1px;\n"
"background-color: rgb(211, 35, 0);")
        self.Abort_btn3.setText("")
        self.Abort_btn3.setObjectName("Abort_btn3")
        self.Mode_TMS_btn4 = ClickableLabel(self.centralwidget)
        self.Mode_TMS_btn4.setGeometry(QtCore.QRect(72, 550, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Mode_TMS_btn4.setFont(font)
        self.Mode_TMS_btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_TMS_btn4.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 8pt \"Inter\";")
        self.Mode_TMS_btn4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mode_TMS_btn4.setObjectName("Mode_TMS_btn4")
        self.Mode_TMS_btn2 = ClickableLabel(self.centralwidget)
        self.Mode_TMS_btn2.setGeometry(QtCore.QRect(40, 540, 21, 21))
        self.Mode_TMS_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_TMS_btn2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Mode_TMS_btn2.setText("")
        self.Mode_TMS_btn2.setPixmap(QtGui.QPixmap("img/TMS.png"))
        self.Mode_TMS_btn2.setScaledContents(True)
        self.Mode_TMS_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode_TMS_btn2.setPixmap(QtGui.QPixmap(str(TMS_img_path)))
        self.Mode_TMS_btn3 = ClickableLabel(self.centralwidget)
        self.Mode_TMS_btn3.setGeometry(QtCore.QRect(72, 536, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter 18pt")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Mode_TMS_btn3.setFont(font)
        self.Mode_TMS_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_TMS_btn3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Inter 18pt\";")
        self.Mode_TMS_btn3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mode_TMS_btn3.setObjectName("Mode_TMS_btn3")
        self.Mode_TMS_btn1 = ClickableLabel(self.centralwidget)
        self.Mode_TMS_btn1.setGeometry(QtCore.QRect(27, 529, 141, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Mode_TMS_btn1.setFont(font)
        self.Mode_TMS_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_TMS_btn1.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(20, 20, 20);")
        self.Mode_TMS_btn1.setText("")
        self.Mode_TMS_btn1.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode_TMS_btn1.setObjectName("Mode_TMS_btn1")
        self.Mode_Box = QtWidgets.QLabel(self.centralwidget)
        self.Mode_Box.setGeometry(QtCore.QRect(22, 524, 152, 97))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Mode_Box.setFont(font)
        self.Mode_Box.setStyleSheet("border-radius :15px;\n"
"background-color: rgb(0, 0, 0,170);")
        self.Mode_Box.setText("")
        self.Mode_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode_Box.setObjectName("Mode_Box")
        self.Mode_Flight_btn1 = ClickableLabel(self.centralwidget)
        self.Mode_Flight_btn1.setGeometry(QtCore.QRect(37, 584, 25, 25))
        self.Mode_Flight_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_Flight_btn1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Mode_Flight_btn1.setText("")
        flight_img_path = Path(__file__).parent / "img" / "flight.png"
        self.Mode_Flight_btn1.setPixmap(QtGui.QPixmap(str(flight_img_path)))
        self.Mode_Flight_btn1.setScaledContents(True)
        self.Mode_Flight_btn1.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode_Flight_btn1.setObjectName("Mode_Flight_btn1")
        self.Mode_Flight_btn4 = ClickableLabel(self.centralwidget)
        self.Mode_Flight_btn4.setGeometry(QtCore.QRect(28, 575, 141, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Mode_Flight_btn4.setFont(font)
        self.Mode_Flight_btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_Flight_btn4.setStyleSheet("border-radius :10px;\n"
"background-color: rgb(20, 20, 20);")
        self.Mode_Flight_btn4.setText("")
        self.Mode_Flight_btn4.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode_Flight_btn4.setObjectName("Mode_Flight_btn4")
        self.Mode_Flight_btn3 = ClickableLabel(self.centralwidget)
        self.Mode_Flight_btn3.setGeometry(QtCore.QRect(73, 596, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Mode_Flight_btn3.setFont(font)
        self.Mode_Flight_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_Flight_btn3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 8pt \"Inter\";")
        self.Mode_Flight_btn3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mode_Flight_btn3.setObjectName("Mode_Flight_btn3")
        self.Mode_Flight_btn2 = ClickableLabel(self.centralwidget)
        self.Mode_Flight_btn2.setGeometry(QtCore.QRect(73, 582, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter 18pt")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Mode_Flight_btn2.setFont(font)
        self.Mode_Flight_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode_Flight_btn2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Inter 18pt\";")
        self.Mode_Flight_btn2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mode_Flight_btn2.setObjectName("Mode_Flight_btn2")
        self.Program_Info_Box = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Box.setGeometry(QtCore.QRect(880, 90, 371, 241))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Program_Info_Box.setFont(font)
        self.Program_Info_Box.setStyleSheet("border-radius :13px;\n"
"background-color: rgb(0, 0, 0);")
        self.Program_Info_Box.setText("")
        self.Program_Info_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Program_Info_Box.setObjectName("Program_Info_Box")
        self.feedback_Box = QtWidgets.QLabel(self.centralwidget)
        self.feedback_Box.setGeometry(QtCore.QRect(930, 22, 261, 51))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.feedback_Box.setFont(font)
        self.feedback_Box.setStyleSheet("border-radius :13px;\n"
"background-color: rgb(0, 0, 0,130);")
        self.feedback_Box.setText("")
        self.feedback_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.feedback_Box.setObjectName("feedback_Box")
        self.feedback_Info = QtWidgets.QLabel(self.centralwidget)
        self.feedback_Info.setGeometry(QtCore.QRect(981, 47, 180, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.feedback_Info.setFont(font)
        self.feedback_Info.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Inter\";")
        self.feedback_Info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.feedback_Info.setObjectName("feedback_Info")
        self.feedback_Title = QtWidgets.QLabel(self.centralwidget)
        self.feedback_Title.setGeometry(QtCore.QRect(981, 30, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.feedback_Title.setFont(font)
        self.feedback_Title.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Inter\";")
        self.feedback_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.feedback_Title.setObjectName("feedback_Title")
        self.feedback_logo = QtWidgets.QLabel(self.centralwidget)
        self.feedback_logo.setGeometry(QtCore.QRect(943, 35, 25, 25))
        self.feedback_logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.feedback_logo.setText("")
        feedback_img_path = Path(__file__).parent / "img" / "feedback.png"
        self.feedback_logo.setPixmap(QtGui.QPixmap(str(feedback_img_path)))
        self.feedback_logo.setScaledContents(True)
        self.feedback_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.feedback_logo.setObjectName("feedback_logo")
        self.Flight_interface_Safty_btn = ClickableLabel(self.centralwidget)
        self.Flight_interface_Safty_btn.setGeometry(QtCore.QRect(388, 649, 25, 25))
        self.Flight_interface_Safty_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_Safty_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_Safty_btn.setText("")
        unsafty_img_path = Path(__file__).parent / "img" / "safty_unlocked.png"
        self.Flight_interface_Safty_btn.setPixmap(QtGui.QPixmap(str(unsafty_img_path)))
        self.Flight_interface_Safty_btn.setScaledContents(True)
        self.Flight_interface_Safty_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_Safty_btn.setObjectName("Flight_interface_Safty_btn")
        self.Program_Info_Text1 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text1.setGeometry(QtCore.QRect(440, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Program_Info_Text1.setFont(font)
        self.Program_Info_Text1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25pt \"Inter\";")
        self.Program_Info_Text1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text1.setObjectName("Program_Info_Text1")
        self.Program_Info_Text2 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text2.setGeometry(QtCore.QRect(500, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Text2.setFont(font)
        self.Program_Info_Text2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 25pt \"Inter\";")
        self.Program_Info_Text2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text2.setObjectName("Program_Info_Text2")
        self.Program_Info_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Logo.setGeometry(QtCore.QRect(430, 130, 61, 61))
        self.Program_Info_Logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Program_Info_Logo.setText("")
        logo_img_path = Path(__file__).parent / "img" / "Flash_logo.png"
        self.Program_Info_Logo.setPixmap(QtGui.QPixmap(str(logo_img_path)))
        self.Program_Info_Logo.setScaledContents(True)
        self.Program_Info_Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Program_Info_Logo.setObjectName("Program_Info_Logo")
        self.Program_Info_Text3 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text3.setGeometry(QtCore.QRect(440, 250, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Text3.setFont(font)
        self.Program_Info_Text3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 13pt \"Inter\";")
        self.Program_Info_Text3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text3.setObjectName("Program_Info_Text3")
        self.Program_Info_Text6 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text6.setGeometry(QtCore.QRect(440, 410, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Text6.setFont(font)
        self.Program_Info_Text6.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 10pt \"Inter\";")
        self.Program_Info_Text6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text6.setObjectName("Program_Info_Text6")
        self.Program_Info_Text4 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text4.setGeometry(QtCore.QRect(440, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Text4.setFont(font)
        self.Program_Info_Text4.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 10pt \"Inter\";")
        self.Program_Info_Text4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text4.setObjectName("Program_Info_Text4")
        self.Program_Info_Text5 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text5.setGeometry(QtCore.QRect(440, 300, 271, 201))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Text5.setFont(font)
        self.Program_Info_Text5.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 8pt \"Inter\";")
        self.Program_Info_Text5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text5.setObjectName("Program_Info_Text5")
        self.feedback_time = QtWidgets.QLabel(self.centralwidget)
        self.feedback_time.setGeometry(QtCore.QRect(1141, 30, 35, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 18pt")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.feedback_time.setFont(font)
        self.feedback_time.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(167, 167, 167);\n"
"font: 8pt \"Inter 18pt\";")
        self.feedback_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.feedback_time.setObjectName("feedback_time")
        self.Flight_interface_ModeDN_btn5 = ClickableLabel(self.centralwidget)
        self.Flight_interface_ModeDN_btn5.setGeometry(QtCore.QRect(154, 657, 10, 6))
        self.Flight_interface_ModeDN_btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Flight_interface_ModeDN_btn5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Flight_interface_ModeDN_btn5.setText("")
        mode_down_img_path = Path(__file__).parent / "img" / "mode_down.png"
        self.Flight_interface_ModeDN_btn5.setPixmap(QtGui.QPixmap(str(mode_down_img_path)))
        self.Flight_interface_ModeDN_btn5.setScaledContents(True)
        self.Flight_interface_ModeDN_btn5.setAlignment(QtCore.Qt.AlignCenter)
        self.Flight_interface_ModeDN_btn5.setObjectName("Flight_interface_ModeDN_btn5")
        self.confirm_box = QtWidgets.QLabel(self.centralwidget)
        self.confirm_box.setGeometry(QtCore.QRect(0, 0, 1281, 711))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.confirm_box.setFont(font)
        self.confirm_box.setStyleSheet("border-radius :13px;\n"
"background-color: rgb(0, 0, 0,200);")
        self.confirm_box.setText("")
        self.confirm_box.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_box.setObjectName("confirm_box")
        self.confirm_logo = QtWidgets.QLabel(self.centralwidget)
        self.confirm_logo.setGeometry(QtCore.QRect(620, 240, 61, 61))
        self.confirm_logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.confirm_logo.setText("")
        sequence_img_path = Path(__file__).parent / "img" / "Sequence.png"
        self.confirm_logo.setPixmap(QtGui.QPixmap(str(sequence_img_path)))
        self.confirm_logo.setScaledContents(True)
        self.confirm_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_logo.setObjectName("confirm_logo")
        self.confirm_text1 = QtWidgets.QLabel(self.centralwidget)
        self.confirm_text1.setGeometry(QtCore.QRect(520, 310, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.confirm_text1.setFont(font)
        self.confirm_text1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 20pt \"Inter\";")
        self.confirm_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_text1.setObjectName("confirm_text1")
        
        self.LP_text1 = QtWidgets.QLabel(self.centralwidget)
        self.LP_text1.setGeometry(QtCore.QRect(720, 330, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LP_text1.setFont(font)
        self.LP_text1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 20pt \"Inter\";")
        self.LP_text1.setAlignment(QtCore.Qt.AlignLeft)
        self.LP_text1.setObjectName("confirm_text1")

        self.confirm_text2 = QtWidgets.QLabel(self.centralwidget)
        self.confirm_text2.setGeometry(QtCore.QRect(460, 340, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.confirm_text2.setFont(font)
        self.confirm_text2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 15pt \"Inter\";")
        self.confirm_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_text2.setObjectName("LP_text1")

        self.LP_text2 = QtWidgets.QLabel(self.centralwidget)
        self.LP_text2.setGeometry(QtCore.QRect(720, 370, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.LP_text2.setFont(font)
        self.LP_text2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 15pt \"Inter\";")
        self.LP_text2.setAlignment(QtCore.Qt.AlignLeft)
        self.LP_text2.setObjectName("LP_text2")

        self.confirm_btn1 = ClickableLabel(self.centralwidget)
        self.confirm_btn1.setGeometry(QtCore.QRect(610, 400, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 24pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.confirm_btn1.setFont(font)
        self.confirm_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirm_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 15pt \"Inter 24pt\";\n"
"color: rgb(28, 115, 255);")
        self.confirm_btn1.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_btn1.setObjectName("confirm_btn1")
        self.confirm_btn2 = ClickableLabel(self.centralwidget)
        self.confirm_btn2.setGeometry(QtCore.QRect(600, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.confirm_btn2.setFont(font)
        self.confirm_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirm_btn2.setStyleSheet("border-radius :9px;\n"
"background-color: rgb(54, 159, 255,60);")
        self.confirm_btn2.setText("")
        self.confirm_btn2.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_btn2.setObjectName("confirm_btn2")
        self.confirm_exit_btn = ClickableLabel(self.centralwidget)
        self.confirm_exit_btn.setGeometry(QtCore.QRect(590, 440, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.confirm_exit_btn.setFont(font)
        self.confirm_exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirm_exit_btn.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(178, 178, 178);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 11pt \"Inter\";")
        self.confirm_exit_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_exit_btn.setObjectName("confirm_exit_btn")

        self.LP_exit_btn = ClickableLabel(self.centralwidget)
        self.LP_exit_btn.setGeometry(QtCore.QRect(720, 430, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.LP_exit_btn.setFont(font)
        self.LP_exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LP_exit_btn.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(178, 178, 178);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 11pt \"Inter\";")
        self.LP_exit_btn.setAlignment(QtCore.Qt.AlignLeft)
        self.LP_exit_btn.setObjectName("confirm_exit_btn")

        self.Program_Info_Exit_btn = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Exit_btn.setGeometry(QtCore.QRect(1210, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Exit_btn.setFont(font)
        self.Program_Info_Exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Program_Info_Exit_btn.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 20pt \"Inter\";")
        self.Program_Info_Exit_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.Program_Info_Exit_btn.setObjectName("Program_Info_Exit_btn")
        self.Control_confirm_btn1 = ClickableLabel(self.centralwidget)
        self.Control_confirm_btn1.setGeometry(QtCore.QRect(40, 540, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Control_confirm_btn1.setFont(font)
        self.Control_confirm_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_confirm_btn1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(30,144,255);\n"
"font: 25 10pt \"Inter\";")
        self.Control_confirm_btn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Control_confirm_btn1.setObjectName("Control_confirm_btn1")
        self.Control_Sequence_btn3 = ClickableLabel(self.centralwidget)
        self.Control_Sequence_btn3.setGeometry(QtCore.QRect(60, 585, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 24pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Control_Sequence_btn3.setFont(font)
        self.Control_Sequence_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_Sequence_btn3.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 15pt \"Inter 24pt\";\n"
"color: rgb(28, 115, 255);")
        self.Control_Sequence_btn3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Control_Sequence_btn3.setObjectName("Control_Sequence_btn3")
        self.Control_confirm_btn2 = ClickableLabel(self.centralwidget)
        self.Control_confirm_btn2.setGeometry(QtCore.QRect(40, 590, 2, 15))
        self.Control_confirm_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_confirm_btn2.setStyleSheet("border-radius :1px;\n"
"background-color: rgb(43, 162, 255);")
        self.Control_confirm_btn2.setText("")
        self.Control_confirm_btn2.setObjectName("Control_confirm_btn2")

        self.HW_connect_check_bar = ClickableLabel(self.centralwidget)
        self.HW_connect_check_bar.setGeometry(QtCore.QRect(70, 590, 2, 15))
        self.HW_connect_check_bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HW_connect_check_bar.setStyleSheet("border-radius :1px;\n"
"background-color: rgb(43, 162, 255);")
        self.HW_connect_check_bar.setText("")
        self.HW_connect_check_bar.setObjectName("HW_connect_check_bar")

        self.Control_Sequence_btn4 = ClickableLabel(self.centralwidget)
        self.Control_Sequence_btn4.setGeometry(QtCore.QRect(30, 535, 81, 81))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Control_Sequence_btn4.setFont(font)
        self.Control_Sequence_btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Control_Sequence_btn4.setStyleSheet("border-radius :9px;\n"
"background-color: rgb(54, 159, 255,60);")
        self.Control_Sequence_btn4.setText("")
        self.Control_Sequence_btn4.setAlignment(QtCore.Qt.AlignCenter)
        self.Control_Sequence_btn4.setObjectName("Control_Sequence_btn4")
        self.interface_box = QtWidgets.QLabel(self.centralwidget)
        self.interface_box.setGeometry(QtCore.QRect(95, 175, 1090, 345))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.interface_box.setFont(font)
        self.interface_box.setStyleSheet("border-radius :5px;\n"
"background-color: rgb(15, 15, 15,150);")
        self.interface_box.setText("")
        self.interface_box.setAlignment(QtCore.Qt.AlignCenter)
        self.interface_box.setObjectName("interface_box")

        self.terminal_main = QtWidgets.QTextBrowser(self.centralwidget)
        self.terminal_main.setGeometry(QtCore.QRect(820, 180, 360, 335))
        self.terminal_main.setStyleSheet("border-radius :5px;\n"
"background-color: rgb(0, 0, 0,150);\n"
"color: rgb(255, 255, 255);")
        self.terminal_main.setObjectName("terminal_main")
        
        self.Chart_box = QtWidgets.QLabel(self.centralwidget)
        self.Chart_box.setGeometry(QtCore.QRect(200, 170, 1061, 331))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Chart_box.setFont(font)
        self.Chart_box.setStyleSheet("border-radius :7px;\n"
"background-color: rgb(0, 0, 0,150);")
        self.Chart_box.setText("")
        self.Chart_box.setAlignment(QtCore.Qt.AlignCenter)
        self.Chart_box.setObjectName("Chart_box")

        pg.setConfigOptions(antialias=True)  # 곡선 부드럽게

        # 전체 테마 설정
        pg.setConfigOption('background', '#1e1e1e')  # 다크 모드 배경
        pg.setConfigOption('foreground', 'white')    # 축/글자 흰색

        self.Chart_1 = pg.PlotWidget(MainWindow, title="Thrust") 
        self.Chart_1.setGeometry(QtCore.QRect(100, 180, 341, 165))
        self.Chart_1.setStyleSheet("border-radius :7px;\n"
"background-color: rgb(0, 0, 0, 100);")
        self.Chart_1.setObjectName("Chart_1")
        self.Chart_1.setBackground(QColor(0, 0, 0, 0)) 

        self.Chart_2 = pg.PlotWidget(MainWindow, title="Pressure") 
        self.Chart_2.setGeometry(QtCore.QRect(100, 350, 341, 165))
        self.Chart_2.setStyleSheet("border-radius :7px;\n"
"background-color: rgb(0, 0, 0, 100);")
        self.Chart_2.setObjectName("Chart_2")
        self.Chart_2.setBackground(QColor(0, 0, 0, 0)) 
        
        #self.Chart_3 = gl.GLViewWidget(MainWindow)
        #self.Chart_3.setGeometry(QtCore.QRect(445, 180, 371, 335))
        #self.Chart_3.setObjectName("Chart_3")
        #self.Chart_3.setCameraPosition(distance=40)
        #self.Chart_3.setStyleSheet("border-radius :7px; background-color: rgba(0, 0, 0, 0);")

        # 좌표축 추가
        #axes = gl.GLAxisItem()
        #axes.setSize(x=10, y=10, z=10)
        #self.Chart_3.addItem(axes)

        # 3D 점 추가
        #self.scatter_plot = gl.GLScatterPlotItem(pos=np.array([[0,0,0]]), color=(1,0,0,1), size=5)
        #self.Chart_3.addItem(self.scatter_plot)

        self.Chart_box_2 = QtWidgets.QLabel(self.centralwidget)
        self.Chart_box_2.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.Chart_box_2.setFont(font)
        self.Chart_box_2.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.Chart_box_2.setText("")
        self.Chart_box_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Chart_box_2.setObjectName("Chart_box_2")
        self.Program_Info_Text2_2 = QtWidgets.QLabel(self.centralwidget)
        self.Program_Info_Text2_2.setGeometry(QtCore.QRect(532, 240, 111, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(80)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Program_Info_Text2_2.setFont(font)
        self.Program_Info_Text2_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 80pt \"Inter\";")
        self.Program_Info_Text2_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Program_Info_Text2_2.setObjectName("Program_Info_Text2_2")
        self.intro_img_2 = QtWidgets.QLabel(self.centralwidget)
        self.intro_img_2.setGeometry(QtCore.QRect(60, 130, 211, 90))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(80)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.intro_img_2.setFont(font)
        self.intro_img_2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 80pt \"Inter\";")
        self.intro_img_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_img_2.setObjectName("intro_img_2")
        self.intro_text1 = QtWidgets.QLabel(self.centralwidget)
        intro_img_path = Path(__file__).parent / "img" / "intro_logo.png"
        self.intro_img_2.setPixmap(QtGui.QPixmap(str(intro_img_path)))
        self.intro_img_2.setScaledContents(True)
        self.intro_img_2.setGeometry(QtCore.QRect(70, 150, 331, 98))

        self.LP_level_img = ClickableLabel(self.centralwidget)
        self.LP_level_img.setGeometry(QtCore.QRect(270, 180, 321, 301))
        self.LP_level_img.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.LP_level_img.setText("")
        LP_level_img_path = Path(__file__).parent / "img" / "L_P.png"
        self.LP_level_img.setPixmap(QtGui.QPixmap(str(LP_level_img_path)))
        self.LP_level_img.setScaledContents(True)
        self.LP_level_img.setAlignment(QtCore.Qt.AlignCenter)
        self.LP_level_img.setObjectName("LP_level_img")

        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.intro_text1.setFont(font)
        self.intro_text1.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 40pt \"Inter\";")
        self.intro_text1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_text1.setObjectName("intro_text1")
        self.intro_HW_main = QtWidgets.QLabel(self.centralwidget)
        self.intro_HW_main.setGeometry(QtCore.QRect(70, 550, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.intro_HW_main.setFont(font)
        self.intro_HW_main.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 20pt \"Inter\";")
        self.intro_HW_main.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_HW_main.setObjectName("intro_HW_main")
        self.intro_HW_text = QtWidgets.QLabel(self.centralwidget)
        self.intro_HW_text.setGeometry(QtCore.QRect(70, 530, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(1)
        self.intro_HW_text.setFont(font)
        self.intro_HW_text.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 12 italic 13pt \"Inter\";")
        self.intro_HW_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_HW_text.setObjectName("intro_HW_text")
        self.intro_strart_btn2 = ClickableLabel(self.centralwidget)
        self.intro_strart_btn2.setGeometry(QtCore.QRect(124, 629, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Inter 24pt")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.intro_strart_btn2.setFont(font)
        self.intro_strart_btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.intro_strart_btn2.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 15pt \"Inter 24pt\";\n"
"color: rgb(28, 115, 255);")
        self.intro_strart_btn2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_strart_btn2.setObjectName("intro_strart_btn2")
        self.intro_strart_btn1 = ClickableLabel(self.centralwidget)
        self.intro_strart_btn1.setGeometry(QtCore.QRect(63, 620, 151, 41))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoSB00")
        font.setPointSize(11)
        self.intro_strart_btn1.setFont(font)
        self.intro_strart_btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.intro_strart_btn1.setStyleSheet("border-radius :9px;\n"
"background-color: rgb(54, 159, 255,60);")
        self.intro_strart_btn1.setText("")
        self.intro_strart_btn1.setAlignment(QtCore.Qt.AlignCenter)
        self.intro_strart_btn1.setObjectName("intro_strart_btn1")
        self.intro_strart_btn3 = ClickableLabel(self.centralwidget)
        self.intro_strart_btn3.setGeometry(QtCore.QRect(73, 633, 2, 15))
        self.intro_strart_btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.intro_strart_btn3.setStyleSheet("border-radius :1px;\n"
"background-color: rgb(43, 162, 255);")
        self.intro_strart_btn3.setText("")
        self.intro_strart_btn3.setObjectName("intro_strart_btn3")
        self.intro_HW_img = QtWidgets.QLabel(self.centralwidget)
        self.intro_HW_img.setGeometry(QtCore.QRect(80, 590, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.intro_HW_img.setFont(font)
        self.intro_HW_img.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 25 20pt \"Inter\";")
        self.intro_HW_img.setText("")
        connect_img_path = Path(__file__).parent / "img" / "connect.png"
        self.intro_HW_img.setPixmap(QtGui.QPixmap(str(connect_img_path)))
        self.intro_HW_img.setScaledContents(True)
        self.intro_HW_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_HW_img.setObjectName("intro_HW_img")
        self.intro_img = QtWidgets.QLabel(self.centralwidget)
        self.intro_img.setGeometry(QtCore.QRect(560, 130, 721, 531))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(80)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.intro_img.setFont(font)
        self.intro_img.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 80pt \"Inter\";")
        self.intro_img.setText("")
        intro_img_path = Path(__file__).parent / "img" / "intro.png"
        self.intro_img.setPixmap(QtGui.QPixmap(str(intro_img_path)))
        self.intro_img.setScaledContents(True)
        self.intro_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.intro_img.setObjectName("intro_img")

        self.back_grad_up.raise_()
        self.back_grad_down.raise_()
        self.Program_Info_Logo.raise_()
        self.Program_Info_Logo.hide()
        self.Control_box.hide()
        self.Control_HWCheck_btn4.raise_()
        self.interface_box.raise_()
        self.terminal_main.raise_()
        self.Control_Sequence_btn3.raise_()
        self.Control_Sequence_btn4.raise_()
        self.confirm_btn2.raise_()
        self.Control_1ignition_btn2.raise_()
        self.Mode_Box.raise_()
        self.Mode_Flight_btn4.raise_()
        self.Mode_TMS_btn1.raise_()
        self.Mode_TMS_btn2.raise_()
        self.Mode_TMS_btn4.raise_()
        self.Mode_TMS_btn3.raise_()
        self.Mode_Flight_btn1.raise_()
        self.Mode_Flight_btn3.raise_()
        self.Mode_Flight_btn2.raise_()
        self.Abort_Box.raise_()
        self.parameter2_box.raise_()
        self.Sequence_time_text.raise_()
        self.parameter1_box.raise_()
        self.parameter1_text2.raise_()
        self.parameter1_text1.raise_()
        self.Flight_interface_Box.raise_()
        self.parameter1_main.raise_()
        #self.Abort_text.raise_()
        self.flight_info_text.raise_()
        self.flight_data_text.raise_()
        self.Flight_interface_Mode_btn1.raise_()
        self.Flight_interface_Mode_btn2.raise_()
        self.Flight_interface_Mode_btn3.raise_()
        self.Flight_interface_Time.raise_()
        self.Flight_interface_Control_btn.raise_()
        self.Flight_interface_export_btn.raise_()
        self.Flight_interface_chart_btn.raise_()
        self.Flight_interface_seting_btn.raise_()
        self.Flight_interface_line4.raise_()
        self.Flight_interface_line2.raise_()
        self.Flight_interface_line3.raise_()
        self.Flight_interface_line1.raise_()
        self.Flight_interface_Mode_btn4.raise_()
        self.Flight_interface_ModeUP_btn5.raise_()
        self.Control_HWCheck_btn2.raise_()
        self.Control_HWCheck_btn3.raise_()
        self.Control_1ignition_btn1.hide()
        self.Control_1ignition_btn4.raise_()
        self.Control_1ignition_btn3.raise_()
        self.Control_HWCheck_btn1.hide()
        self.Program_Info_btn.raise_()
        self.seq_t_plus10_btn.raise_()
        self.seq_t_minus10_btn.raise_()
        self.re_seq_btn.raise_()
        self.data_reset_btn.raise_()
        self.parameter2_text1.raise_()
        self.parameter2_text2.raise_()
        self.parameter2_main.raise_()
        self.Abort_btn2.raise_()
        self.Abort_btn1.raise_()
        self.Abort_btn3.raise_()
        self.Flight_interface_Safty_btn.raise_()
        self.Flight_interface_ModeDN_btn5.hide()
        self.Program_Info_Exit_btn.hide()
        self.Chart_box.hide()
        #self.Chart_3.hide()
        self.Chart_2.hide()
        self.Chart_1.hide()
        self.gauge_r.raise_()
        self.gauge_b.raise_()
        self.Chart_box_2.raise_()
        self.step.raise_()

        self.intro_img_2.raise_()
        self.intro_HW_main.raise_()
        self.intro_HW_text.raise_()
        self.intro_strart_btn1.raise_()
        self.intro_strart_btn2.raise_()
        self.intro_strart_btn3.raise_()
        self.intro_HW_img.raise_()
        self.intro_img.raise_()
        self.HW_connect_check_bar.raise_()
        self.Control_confirm_btn2.raise_()
        self.confirm_box.raise_()
        self.confirm_logo.raise_()
        self.confirm_text1.raise_()
        self.confirm_text2.raise_()
        self.confirm_btn1.raise_()
        self.confirm_exit_btn.raise_()
        self.LP_text1.raise_()
        self.LP_text2.raise_()
        self.LP_exit_btn.raise_()
        self.LP_level_img.raise_()

        self.settings_box1.raise_()
        self.Set_title.raise_()
        self.set_desc.raise_()
        self.settings_line.raise_()
        self.settings_box2.raise_()
        self.set_btn_box.raise_()
        self.safty_btn1.raise_()
        self.settings_exit_btn.raise_()
        self.sequence_btn1.raise_()
        self.advanced_btn1.raise_()
        self.data_btn1.raise_()
        self.interface_btn1.raise_()
        self.safty_btn2.raise_()
        self.sequence_btn2.raise_()
        self.data_btn2.raise_()
        self.advanced_btn2.raise_()
        self.interface_btn2.raise_()
        self.settings_text1_1.raise_()
        self.settings_text1_2.raise_()
        self.set_interface2_img_box.raise_()
        self.settings_text2_2.raise_()
        self.settings_text2_1.raise_()
        self.settings_btn1_1.raise_()
        self.settings_btn1_2.raise_()
        self.settings_btn1_3.raise_()
        self.set_a_btn2.raise_()
        self.set_a_btn3_2.raise_()
        self.set_a_btn3.raise_()
        self.set_interface2_img.raise_()
        self.settings_text2_3.raise_()
        self.settings_btn2_1.raise_()
        self.settings_btn2_3.raise_()
        self.settings_btn2_2.raise_()
        self.programinfo_btn1.raise_()
        self.programinfo_btn2.raise_()
        self.settings_text3_2.raise_()
        self.settings_text3_1.raise_()
        self.set_interface3_Cbtn1.raise_()
        self.set_interface3_Cbtn2.raise_()
        self.checkBox_3.raise_()
        self.set_interface3_Cbtn3.raise_()
        self.set_a_spinbox1.raise_()
        self.set_a_spin1.raise_()
        self.feedback_Box.raise_()
        self.feedback_Info.raise_()
        self.feedback_Title.raise_()
        self.feedback_logo.raise_()
        self.feedback_time.raise_()
        self.Program_Info_Box.raise_()
        self.Program_Info_Text1.raise_()
        self.Program_Info_Text2.raise_()
        self.Program_Info_Text3.raise_()
        self.Program_Info_Text4.raise_()
        self.Program_Info_Text5.raise_()
        self.Program_Info_Logo.raise_()

        self.Program_Info_Text6.hide()

        self.feedback_Box.hide()
        self.feedback_Info.hide()
        self.feedback_Title.hide()
        self.feedback_logo.hide()
        self.feedback_time.hide()

        self.settings_box1.hide()
        self.Set_title.hide()
        self.set_desc.hide()
        self.settings_box2.hide()
        self.set_btn_box.hide()
        self.safty_btn1.hide()
        self.settings_exit_btn.hide()
        self.sequence_btn1.hide()
        self.advanced_btn1.hide()
        self.data_btn1.hide()
        self.interface_btn1.hide()
        self.safty_btn2.hide()
        self.sequence_btn2.hide()
        self.data_btn2.hide()
        self.advanced_btn2.hide()
        self.interface_btn2.hide()
        self.settings_text1_1.hide()
        self.settings_text1_2.hide()
        self.set_interface2_img_box.hide()
        self.settings_text2_2.hide()
        self.settings_text2_1.hide()
        self.settings_btn1_1.hide()
        self.settings_btn1_2.hide()
        self.settings_btn1_3.hide()
        self.set_a_btn2.hide()
        self.set_a_btn3_2.hide()
        self.set_a_btn3.hide()
        self.set_interface2_img.hide()
        self.settings_text2_3.hide()
        self.settings_btn2_1.hide()
        self.settings_btn2_3.hide()
        self.settings_btn2_2.hide()
        self.programinfo_btn1.hide()
        self.programinfo_btn2.hide()
        self.settings_text3_2.hide()
        self.settings_text3_1.hide()
        self.set_interface3_Cbtn1.hide()
        self.set_interface3_Cbtn2.hide()
        self.checkBox_3.hide()
        self.set_interface3_Cbtn3.hide()
        self.set_a_spinbox1.hide()
        self.set_a_spin1.hide()
        self.settings_line.hide()


        self.LP_level_img.hide()
        self.LP_text1.hide()
        self.LP_text2.hide()
        self.LP_exit_btn.hide()
        self.Control_confirm_btn1.hide()
        self.Control_confirm_btn2.hide()

        self.Program_Info_Box.hide()
        self.Program_Info_Text1.hide()
        self.Program_Info_Text2.hide()
        self.Program_Info_Text3.hide()
        self.Program_Info_Text4.hide()
        self.Program_Info_Text5.hide()
        self.Program_Info_Logo.hide()
        self.step.hide()
        self.confirm_box.hide()
        self.confirm_btn1.hide()
        self.confirm_btn2.hide()
        self.confirm_logo.hide()
        self.confirm_text2.hide()
        self.confirm_exit_btn.hide()
        self.confirm_text1.hide()

        self.set_interface3_Cbtn1.setChecked(True)
        self.set_interface3_Cbtn2.setChecked(False)
        self.set_interface3_Cbtn3.setChecked(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.re_seq_btn.clicked.connect(self.seq_reset)
        
        self.seq_t_minus10_btn.clicked.connect(self.seq_tm10)
        self.seq_t_plus10_btn.clicked.connect(self.seq_tp10)



        self.intro_strart_btn1.clicked.connect(self.intro_exit)
        self.intro_strart_btn2.clicked.connect(self.intro_exit)
        self.intro_strart_btn3.clicked.connect(self.intro_exit)
        self.Mode_Flight_btn1.clicked.connect(self.Mode_Flight)
        self.Mode_Flight_btn2.clicked.connect(self.Mode_Flight)
        self.Mode_Flight_btn3.clicked.connect(self.Mode_Flight)
        self.Mode_Flight_btn4.clicked.connect(self.Mode_Flight)
        self.Mode_TMS_btn1.clicked.connect(self.Mode_TMS)
        self.Mode_TMS_btn2.clicked.connect(self.Mode_TMS)
        self.Mode_TMS_btn3.clicked.connect(self.Mode_TMS)
        self.Mode_TMS_btn4.clicked.connect(self.Mode_TMS)
        self.LP_exit_btn.clicked.connect(self.LP_stop)


        self.Flight_interface_Control_btn.clicked.connect(self.Control_btn)
        self.Flight_interface_export_btn.clicked.connect(self.export)
        self.Flight_interface_chart_btn.clicked.connect(self.chart)
        self.Flight_interface_Safty_btn.clicked.connect(self.safty)
        self.Flight_interface_seting_btn.clicked.connect(self.setting)

        self.confirm_exit_btn.clicked.connect(self.confirm_exit)
        self.confirm_btn1.clicked.connect(self.Confirm)
        self.confirm_btn2.clicked.connect(self.Confirm)

        self.Abort_btn1.clicked.connect(self.abort)
        self.Abort_btn2.clicked.connect(self.abort)
        self.Abort_btn3.clicked.connect(self.abort)

        self.Flight_interface_Mode_btn1.clicked.connect(self.Mode_chage_btn)
        self.Flight_interface_Mode_btn2.clicked.connect(self.Mode_chage_btn)
        self.Flight_interface_Mode_btn3.clicked.connect(self.Mode_chage_btn)
        self.Flight_interface_Mode_btn4.clicked.connect(self.Mode_chage_btn)
        self.Flight_interface_ModeUP_btn5.clicked.connect(self.Mode_chage_btn)
        self.Flight_interface_ModeDN_btn5.clicked.connect(self.Mode_chage_btn)
        self.Program_Info_btn.clicked.connect(self.program_info)
        self.data_reset_btn.clicked.connect(self.data_reset)
        
        self.Control_1ignition_btn1.clicked.connect(self.Manual_Ignition)
        self.Control_1ignition_btn2.clicked.connect(self.Manual_Ignition)
        self.Control_1ignition_btn3.clicked.connect(self.Manual_Ignition)
        self.Control_1ignition_btn4.clicked.connect(self.Manual_Ignition)
        self.Control_HWCheck_btn1.clicked.connect(self.LP_toggle)
        self.Control_HWCheck_btn2.clicked.connect(self.LP_toggle)
        self.Control_HWCheck_btn3.clicked.connect(self.LP_toggle)
        self.Control_HWCheck_btn4.clicked.connect(self.LP_toggle)
        self.Control_confirm_btn1.clicked.connect(self.sequence)
        self.Control_confirm_btn2.clicked.connect(self.sequence)   
        self.Control_Sequence_btn3.clicked.connect(self.sequence)
        self.Control_Sequence_btn4.clicked.connect(self.sequence)
        self.settings_exit_btn.clicked.connect(self.settings_exit)

        self.settings_btn1_1.clicked.connect(self.settings_btn1)
        self.settings_btn1_2.clicked.connect(self.settings_btn1)
        self.settings_btn1_3.clicked.connect(self.settings_btn1)
        
        self.settings_btn2_1.clicked.connect(self.settings_btn2)
        self.settings_btn2_2.clicked.connect(self.settings_btn2)
        self.settings_btn2_3.clicked.connect(self.settings_btn2)



        self.set_a_btn3_2.clicked.connect(self.gauge_interface_change)
        self.set_a_btn2.clicked.connect(self.gauge_interface_change)

        self.interface_btn1.clicked.connect(self.set_interface)
        self.interface_btn2.clicked.connect(self.set_interface)
        
        self.advanced_btn1.clicked.connect(self.set_advanced)
        self.advanced_btn2.clicked.connect(self.set_advanced)
        self.data_btn1.clicked.connect(self.set_data)
        self.data_btn2.clicked.connect(self.set_data)

        self.sequence_btn1.clicked.connect(self.set_sequence)
        self.sequence_btn2.clicked.connect(self.set_sequence)

        self.safty_btn1.clicked.connect(self.set_safty)
        self.safty_btn2.clicked.connect(self.set_safty)

        self.programinfo_btn1.clicked.connect(self.set_info)
        self.programinfo_btn2.clicked.connect(self.set_info)



        self.set_interface3_Cbtn1.stateChanged.connect(lambda s: self.only_one_checked(s, self.set_interface3_Cbtn1))
        self.set_interface3_Cbtn2.stateChanged.connect(lambda s: self.only_one_checked(s, self.set_interface3_Cbtn2))
        self.set_interface3_Cbtn3.stateChanged.connect(lambda s: self.only_one_checked(s, self.set_interface3_Cbtn3))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flash v4"))
        self.Sequence_time_text.setText(_translate("MainWindow", "T-00"))
        self.parameter1_text2.setText(_translate("MainWindow", "m"))
        self.parameter1_text1.setText(_translate("MainWindow", "ARTITUDE"))
        self.parameter1_main.setText(_translate("MainWindow", "N/A"))
        self.Abort_text.setText(_translate("MainWindow", ""))
        self.flight_info_text.setText(_translate("MainWindow", "No Data - Please Check Signal"))
        self.flight_data_text.setText(_translate("MainWindow", "Data: N/A"))
        self.Flight_interface_Mode_btn2.setText(_translate("MainWindow", "Mode"))
        self.Flight_interface_Mode_btn3.setText(_translate("MainWindow", "TMS Mode"))
        self.Flight_interface_Time.setText(_translate("MainWindow", "12:41:00"))
        self.Control_HWCheck_btn3.setText(_translate("MainWindow", "Start"))
        self.Control_1ignition_btn1.setText(_translate("MainWindow", "강제\n"
"점화"))
        self.Control_1ignition_btn4.setText(_translate("MainWindow", "Start"))
        self.Control_HWCheck_btn1.setText(_translate("MainWindow", "발사대\n"
"기립"))
        self.parameter2_text1.setText(_translate("MainWindow", "ARTITUDE"))
        self.parameter2_text2.setText(_translate("MainWindow", "m"))
        self.parameter2_main.setText(_translate("MainWindow", "N/A"))
        self.Abort_btn1.setText(_translate("MainWindow", "ABORT"))
        self.Mode_TMS_btn4.setText(_translate("MainWindow", "TMS Mode"))
        self.Mode_TMS_btn3.setText(_translate("MainWindow", "TMS"))
        self.Mode_Flight_btn3.setText(_translate("MainWindow", "Flight mode"))
        self.Mode_Flight_btn2.setText(_translate("MainWindow", "Flight"))
        self.feedback_Info.setText(_translate("MainWindow", "안전모드가 활성화 되었습니다!"))
        self.feedback_Title.setText(_translate("MainWindow", "Safty Mode"))
        self.Program_Info_Text1.setText(_translate("MainWindow", "Flash"))
        self.Program_Info_Text2.setText(_translate("MainWindow", "V4"))
        self.Program_Info_Text3.setText(_translate("MainWindow", "macOS Edition"))
        self.Program_Info_Text6.setText(_translate("MainWindow", "© HANWOOL All Rights Reserved"))
        self.Program_Info_Text4.setText(_translate("MainWindow", "HANWOOL FCP Flash V4\n"
"Version: block2"))
        self.Program_Info_Text5.setText(_translate("MainWindow", "Copyright (c) 2025 HANWOOL\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the 'Software'), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE."))
        self.feedback_time.setText(_translate("MainWindow", "12:41"))
        self.confirm_text1.setText(_translate("MainWindow", "시퀀스 활성화"))
        self.confirm_text2.setText(_translate("MainWindow", "시퀀스를 활성화 하시겠습니까?"))
        self.confirm_btn1.setText(_translate("MainWindow", "Confirm"))
        self.confirm_exit_btn.setText(_translate("MainWindow", "← 돌아가기"))

        self.LP_text1.setText(_translate("MainWindow", "발사대 자동 기립중..."))
        self.LP_text2.setText(_translate("MainWindow", "Launch Pad Elevating — 자동 기립 중 \n현재 각도 : 0°"))
        self.LP_exit_btn.setText(_translate("MainWindow", "긴급 정지"))

        self.Program_Info_Exit_btn.setText(_translate("MainWindow", "x"))
        self.Control_confirm_btn1.setText(_translate("MainWindow", "시퀀스\n"
"활성화"))
        self.Control_Sequence_btn3.setText(_translate("MainWindow", "Start"))
        self.terminal_main.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">HANWOOL FCP Flash V4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Version: Block1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-------------------------------------------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Program_Info_Text2_2.setText(_translate("MainWindow", "V4"))
        self.intro_img_2.setText(_translate("MainWindow", ""))
        self.intro_text1.setText(_translate("MainWindow", "welcome to"))
        print(f"{port} = port")
        self.intro_HW_main.setText(_translate("MainWindow", f"{port} Arduino"))
        self.intro_HW_text.setText(_translate("MainWindow", "H/W"))
        self.intro_strart_btn2.setText(_translate("MainWindow", "Start"))

        self.Set_title.setText(_translate("MainWindow", "Interface"))
        self.set_desc.setText(_translate("MainWindow", "이곳에서 인터페이스 설정을 수정할 수 있습니다."))
        self.settings_exit_btn.setText(_translate("MainWindow", "< settings"))
        self.safty_btn1.setText(_translate("MainWindow", "Safty"))
        self.sequence_btn1.setText(_translate("MainWindow", "Sequence"))
        self.advanced_btn1.setText(_translate("MainWindow", "Advanced"))
        self.data_btn1.setText(_translate("MainWindow", "Data"))
        self.interface_btn1.setText(_translate("MainWindow", "Interface"))
        self.settings_text1_1.setText(_translate("MainWindow", "VFS (Voice Feedback System) 활성화"))
        self.settings_text1_2.setText(_translate("MainWindow", "시스템 이벤트를 음성으로 안내하는 기능입니다."))
        self.settings_text2_2.setText(_translate("MainWindow", "센서 데이터를 기반으로 실시간 회전 자세를 모니터 에서 확인할수 있습니다."))
        self.settings_text2_1.setText(_translate("MainWindow", "ADI (Attitude Direction Indicator) 활성화"))
        self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
        self.set_a_btn3_2.setText(_translate("MainWindow", "변경"))
        self.settings_text2_3.setText(_translate("MainWindow", "※ IDA 활성화 시, 자세 시각화를 위한 공간이 확보되어 그래프 출력 영역이 다소 줄어듭니다."))
        self.settings_btn2_2.setText(_translate("MainWindow", "ON"))
        self.programinfo_btn1.setText(_translate("MainWindow", "Program info"))
        self.settings_text3_2.setText(_translate("MainWindow", "게이지의 인터페이스를 수정할수 있습니다."))
        self.settings_text3_1.setText(_translate("MainWindow", "게이지 인터페이스"))
        self.set_interface3_Cbtn1.setText(_translate("MainWindow", "Gauge bar"))
        self.set_interface3_Cbtn2.setText(_translate("MainWindow", "Nomal"))
        self.checkBox_3.setText(_translate("MainWindow", "Nomal"))
        self.set_interface3_Cbtn3.setText(_translate("MainWindow", "None"))

    
    
    def intro_exit(self):
        global intro_exit
        _translate = QtCore.QCoreApplication.translate
        if simulation_mode == 0:
            self.ser.write("IFP_ON".encode())
        t = t_set
        self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
        current_time = datetime.now().strftime("%Y-%m-%d %H")[:-3]
        self.log_entry = f"{current_time} 의 데이터 - Logging initiated\n"
        self.log_entry += "↓ data ↓\n"
        self.log_entry += "--------------------------------------------------------\n"
        intro_exit = 1

        self.HW_connect_check_bar.hide()

        self.interface_box.hide()
        self.terminal_main.hide()

        self.Abort_btn1.hide()
        self.Abort_btn2.hide()
        self.Abort_btn3.hide()
        self.Abort_Box.hide()
        self.Abort_text.hide()

        self.data_reset_btn.hide()
        self.seq_t_plus10_btn.hide()
        self.seq_t_minus10_btn.hide()
        self.re_seq_btn.hide()

        self.Control_confirm_btn2.hide()
        self.Control_Sequence_btn3.hide()
        self.Control_Sequence_btn4.hide()
        self.Control_HWCheck_btn2.hide()
        self.Control_HWCheck_btn3.hide()
        self.Control_HWCheck_btn4.hide()
        self.Control_1ignition_btn2.hide()
        self.Control_1ignition_btn3.hide()
        self.Control_1ignition_btn4.hide()
        self.feedback_Box.hide()
        self.feedback_Info.hide()
        self.feedback_Title.hide()
        self.feedback_logo.hide()
        self.feedback_time.hide()
        self.intro_img_2.hide()
        self.Program_Info_Text2_2.hide()
        self.intro_text1.hide()
        self.intro_HW_main.hide()
        self.intro_HW_text.hide()
        self.intro_strart_btn1.hide()
        self.intro_strart_btn2.hide()
        self.intro_strart_btn3.hide()
        self.intro_HW_img.hide()
        self.intro_img.hide()
        self.Chart_box_2.hide()
        print("intro_exit_btn_Check")
        self.parameter1_text1.setText(_translate("MainWindow", "Thrust"))
        self.parameter1_text2.setText(_translate("MainWindow", "N"))
        self.parameter2_text1.setText(_translate("MainWindow", "Pressure"))
        self.parameter2_text2.setText(_translate("MainWindow", "Mpa"))

        self.TimeUpdateThread = TimeUpdateThread()
        self.TimeUpdateThread.time_signal.connect(self.time)
        self.TimeUpdateThread.start()

        if simulation_mode == 0:
            #시리얼 통신부( 아두이노 없어서 잠시 주석 처리 )
            self.serial_reader_thread = SerialReaderThread(self.ser)
            self.serial_reader_thread.new_data_signal.connect(self.signal)
            self.serial_reader_thread.new_data_signal.connect(self.signal_graph)
            self.serial_reader_thread.new_data_signal.connect(self.gauge)
            self.serial_reader_thread.start()

    def program_info(self):
        global chart_count
        global program_info_count

        
        # #게이지 테스트
        # parameter1_data_g = 321.42
        # parameter2_data_g = 1.12

        # # 추력값을 기반으로 이미지 인덱스 계산 (1~20)
        # index_R = min(int(parameter1_data_g // 25) + 1, 20)

        # # 압력값을 기반으로 이미지 인덱스 계산 (1~20)
        # index_B = min(round(parameter2_data_g / 0.3), 20)
        # index_B = max(index_B, 1)  # 최소값 1 보장

        # # 파일명 포맷: Gauge_B_01.png ~ Gauge_B_20.png
        # filename_r = f"Gauge_R_{index_R:02d}.png"
        # gauge_r_img = Path(__file__).parent / "img" / "gauge" / filename_r
        # self.gauge_r.setPixmap(QtGui.QPixmap(str(gauge_r_img)))

        # # 파일명 포맷: Gauge_B_01.png ~ Gauge_B_20.png
        # filename_b = f"Gauge_B_{index_B:02d}.png"
        # gauge_b_img = Path(__file__).parent / "img" / "gauge" / filename_b
        # self.gauge_b.setPixmap(QtGui.QPixmap(str(gauge_b_img)))
      

        if program_info_count == 1:
            program_info_count = 0
            self.Program_Info_Text1.hide()
            self.Program_Info_Text2.hide()
            self.Program_Info_Logo.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Box.hide()
        else:
            program_info_count = program_info_count+1
            self.Program_Info_Text1.show()
            self.Program_Info_Text2.show()
            self.Program_Info_Logo.show()
            self.Program_Info_Text3.show()
            self.Program_Info_Text4.show()
            self.Program_Info_Text5.show()
            self.Program_Info_Box.show()
        print(f"program_info_btn_Check : {program_info_count}")

    def Mode_chage_btn(self):
        global mode_count
        global control_count
        if mode_count == 1:
            mode_count = 0
            mode_UP_img_path = Path(__file__).parent / "img" / "mode_up.png"
            self.Flight_interface_ModeUP_btn5.setPixmap(QtGui.QPixmap(str(mode_UP_img_path)))
            self.Mode_TMS_btn1.hide()
            self.Mode_Flight_btn4.hide()
            self.Mode_Box.hide()
            self.Mode_TMS_btn4.hide()
            self.Mode_TMS_btn2.hide()
            self.Mode_TMS_btn3.hide()
            self.Mode_Flight_btn1.hide()
            self.Mode_Flight_btn3.hide()
            self.Mode_Flight_btn2.hide()
            self.Mode_TMS_btn2.hide()
        else:
            if control_count == 1:
                control_count = 0
                mode_count = 1
                mode_DN_img_path = Path(__file__).parent / "img" / "mode_down.png"
                self.Flight_interface_ModeUP_btn5.setPixmap(QtGui.QPixmap(str(mode_DN_img_path)))
                self.Mode_TMS_btn1.show()
                self.Mode_Flight_btn4.show()
                self.Mode_Box.show()
                self.Mode_TMS_btn4.show()
                self.Mode_TMS_btn2.show()
                self.Mode_TMS_btn3.show()
                self.Mode_Flight_btn1.show()
                self.Mode_Flight_btn3.show()
                self.Mode_Flight_btn2.show()
                self.Mode_TMS_btn2.show()
                self.Control_box.hide()
                self.Control_HWCheck_btn1.hide()
                self.Control_HWCheck_btn2.hide()
                self.Control_HWCheck_btn3.hide()
                self.Control_HWCheck_btn4.hide()
                self.Control_1ignition_btn1.hide()
                self.Control_1ignition_btn2.hide()
                self.Control_1ignition_btn3.hide()
                self.Control_1ignition_btn4.hide()
                self.Control_confirm_btn1.hide()
                self.Control_confirm_btn2.hide()
                self.Control_Sequence_btn3.hide()
                self.Control_Sequence_btn4.hide()
                self.data_reset_btn.hide()
                self.seq_t_plus10_btn.hide()
                self.seq_t_minus10_btn.hide()
                self.re_seq_btn.hide()
                self.step.hide()
            else:
                mode_count = 1
                mode_DN_img_path = Path(__file__).parent / "img" / "mode_down.png"
                self.Flight_interface_ModeUP_btn5.setPixmap(QtGui.QPixmap(str(mode_DN_img_path)))
                self.Mode_Box.show()
                self.Mode_TMS_btn1.show()
                self.Mode_Flight_btn4.show()
                self.Mode_TMS_btn4.show()
                self.Mode_TMS_btn2.show()
                self.Mode_TMS_btn3.show()
                self.Mode_Flight_btn1.show()
                self.Mode_Flight_btn3.show()
                self.Mode_Flight_btn2.show()
                self.Mode_TMS_btn2.show()
        print(f"mode_chage_btn_Check : {mode_count}")

    def Mode_Flight(self):
        global mode_flight_count
        global mode_TMS_count
        _translate = QtCore.QCoreApplication.translate
        if sequence == 1:
            self.feedback_Title.setText(_translate("MainWindow", "주의"))
            self.feedback_Info.setText(_translate("MainWindow", "시퀀스 진행중 모드 변경 불가합니다!"))
            current_time_2 = datetime.now().strftime("%H:%M")
            self.feedback_time.setText(_translate("MainWindow", current_time_2))
            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()
            QTest.qWait(3000)
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
        else:
            if mode_flight_count == 1:
                print("주의: 이미 플라이트 모드입니다!")
                self.feedback_Title.setText(_translate("MainWindow", "주의"))
                self.feedback_Info.setText(_translate("MainWindow", "이미 플라이트 모드입니다!"))
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()
            else:
                mode_flight_count = 1
                mode_TMS_count = 0
                self.parameter1_text1.setText(_translate("MainWindow", "Speed"))
                self.parameter1_text2.setText(_translate("MainWindow", "m/s"))
                self.parameter2_text1.setText(_translate("MainWindow", "Altitude"))
                self.parameter2_text2.setText(_translate("MainWindow", "m"))
                self.Flight_interface_Mode_btn3.setText(_translate("MainWindow", "Flight Mode"))
                flight_img_path = Path(__file__).parent / "img" / "flight.png"
                self.feedback_Title.setText(_translate("MainWindow", "모드 변경"))
                self.feedback_Info.setText(_translate("MainWindow", "플라이트 모드로 변경되었습니다"))
                self.Flight_interface_Mode_btn4.setPixmap(QtGui.QPixmap(str(flight_img_path)))
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()
        print(f"mode_flight_btn_Check : {mode_count}")

    def Mode_TMS(self):
        global mode_flight_count
        global mode_TMS_count
        global sequence
        _translate = QtCore.QCoreApplication.translate
        if sequence == 1:
            self.feedback_Title.setText(_translate("MainWindow", "주의"))
            self.feedback_Info.setText(_translate("MainWindow", "시퀀스 진행중 모드 변경 불가합니다!"))
            current_time_2 = datetime.now().strftime("%H:%M")
            self.feedback_time.setText(_translate("MainWindow", current_time_2))
            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()
            QTest.qWait(3000)
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
        else:
            if mode_TMS_count == 1:
                print("주의: 이미 TMS 모드입니다!")
                self.feedback_Title.setText(_translate("MainWindow", "주의"))
                self.feedback_Info.setText(_translate("MainWindow", "이미 TMS 모드입니다!"))
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()
            else:
                mode_flight_count = 0
                mode_TMS_count = 1
                self.parameter1_text1.setText(_translate("MainWindow", "Thrust"))
                self.parameter1_text2.setText(_translate("MainWindow", "N"))
                self.parameter2_text1.setText(_translate("MainWindow", "Pressure"))
                self.parameter2_text2.setText(_translate("MainWindow", "Mpa"))
                self.Flight_interface_Mode_btn3.setText(_translate("MainWindow", "TMS Mode"))
                TMS_img_path = Path(__file__).parent / "img" / "TMS.png"
                self.feedback_Title.setText(_translate("MainWindow", "모드 변경"))
                self.feedback_Info.setText(_translate("MainWindow", "TMS 모드로 변경되었습니다"))
                self.Flight_interface_Mode_btn4.setPixmap(QtGui.QPixmap(str(TMS_img_path)))
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()
        print(f"mode_flight_btn_Check : {mode_count}")

    def Control_btn(self):
        global mode_count
        global control_count
        if control_count == 1:
            control_count = 0
            self.data_reset_btn.hide()
            self.seq_t_plus10_btn.hide()
            self.seq_t_minus10_btn.hide()
            self.re_seq_btn.hide()
            self.step.hide()
            self.Control_box.hide()
            self.Control_HWCheck_btn1.hide()
            self.Control_HWCheck_btn2.hide()
            self.Control_HWCheck_btn3.hide()
            self.Control_HWCheck_btn4.hide()
            self.Control_1ignition_btn1.hide()
            self.Control_1ignition_btn2.hide()
            self.Control_1ignition_btn3.hide()
            self.Control_1ignition_btn4.hide()
            self.Control_confirm_btn1.hide()
            self.Control_confirm_btn2.hide()
            self.Control_Sequence_btn3.hide()
            self.Control_Sequence_btn4.hide()
        else:
            if mode_count == 1:
                control_count = 1
                mode_count = 0
                mode_UP_img_path = Path(__file__).parent / "img" / "mode_up.png"
                self.Flight_interface_ModeUP_btn5.setPixmap(QtGui.QPixmap(str(mode_UP_img_path)))
                self.Mode_TMS_btn1.hide()
                self.Mode_Flight_btn4.hide()
                self.Mode_Box.hide()
                self.Mode_TMS_btn4.hide()
                self.Mode_TMS_btn2.hide()
                self.Mode_TMS_btn3.hide()
                self.Mode_Flight_btn1.hide()
                self.Mode_Flight_btn3.hide()
                self.Mode_Flight_btn2.hide()
                self.Mode_TMS_btn2.hide()
                self.data_reset_btn.show()
                self.seq_t_plus10_btn.show()
                self.seq_t_minus10_btn.show()
                self.re_seq_btn.show()
                self.Control_box.show()
                self.step.show()
                self.Control_HWCheck_btn1.show()
                self.Control_HWCheck_btn2.show()
                self.Control_HWCheck_btn3.show()
                self.Control_HWCheck_btn4.show()
                self.Control_1ignition_btn1.show()
                self.Control_1ignition_btn2.show()
                self.Control_1ignition_btn3.show()
                self.Control_1ignition_btn4.show()
                self.Control_confirm_btn1.show()
                self.Control_confirm_btn2.show()
                self.Control_Sequence_btn3.show()
                self.Control_Sequence_btn4.show()
            else:
                control_count = 1
                self.data_reset_btn.show()
                self.seq_t_plus10_btn.show()
                self.seq_t_minus10_btn.show()
                self.re_seq_btn.show()
                self.Control_box.show()
                self.step.show()
                self.Control_HWCheck_btn1.show()
                self.Control_HWCheck_btn2.show()
                self.Control_HWCheck_btn3.show()
                self.Control_HWCheck_btn4.show()
                self.Control_1ignition_btn1.show()
                self.Control_1ignition_btn2.show()
                self.Control_1ignition_btn3.show()
                self.Control_1ignition_btn4.show()
                self.Control_confirm_btn1.show()
                self.Control_confirm_btn2.show()
                self.Control_Sequence_btn3.show()
                self.Control_Sequence_btn4.show()
        print(f"control_btn_Check : {control_count}")

    def safty(self):
        global safty_count
        _translate = QtCore.QCoreApplication.translate

        self.confirm_btn1.hide()
        self.confirm_btn2.hide()
        self.confirm_box.hide()
        self.confirm_logo.hide()
        self.confirm_text2.hide()
        self.confirm_exit_btn.hide()
        self.confirm_text1.hide()

        if sequence == 1:
            self.feedback_Title.setText(_translate("MainWindow", "주의"))
            self.feedback_Info.setText(_translate("MainWindow", "시퀀스가 이미 진행중입니다!"))
            current_time_2 = datetime.now().strftime("%H:%M")
            self.feedback_time.setText(_translate("MainWindow", current_time_2))
            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()
            QTest.qWait(3000)
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
        else:
            if safty_count == 1:
                safty_count = 0

                self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(0,0,0,150));")
                self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,0,0,150), stop:1 rgba(255, 255, 255, 0));")

                unsafty_img_path = Path(__file__).parent / "img" / "safty_unlocked.png"
                self.Flight_interface_Safty_btn.setPixmap(QtGui.QPixmap(str(unsafty_img_path)))
                self.feedback_Title.setText(_translate("MainWindow", "Un Safty"))
                self.feedback_Info.setText(_translate("MainWindow", "안전 모드를 해제하였습니다"))
                print(f"safty_btn_Check : {safty_count}")
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()
            else:
                self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(220,20,60,70));")
                self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220,20,60,70), stop:1 rgba(255, 255, 255, 0));")
                safty_count = 1
                safty_img_path = Path(__file__).parent / "img" / "safty_locked.png"
                self.Flight_interface_Safty_btn.setPixmap(QtGui.QPixmap(str(safty_img_path)))
                self.feedback_Title.setText(_translate("MainWindow", "Safty"))
                self.feedback_Info.setText(_translate("MainWindow", "안전 모드로 변환하였습니다"))
                print(f"safty_btn_Check : {safty_count}")
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()

    def chart(self):
        global chart_count
        global terminal_count
        global program_info_count
        if chart_count == 1:
            chart_count = 0
            self.Chart_1.hide()
            self.Chart_2.hide()
            #self.Chart_3.hide()
            self.interface_box.hide()
            self.terminal_main.hide()
            # self.Chart_box.hide()
        else:
            chart_count = 1
            program_info_count = 0
            self.interface_box.show()
            self.terminal_main.show()
            self.Chart_1.show()
            self.Chart_2.show()
            self.Program_Info_Box.hide()
            self.Program_Info_Text1.hide()
            self.Program_Info_Text2.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Logo.hide()
            if ADI_count == 1:
                self.Chart_2.setGeometry(QtCore.QRect(100, 350, 341, 165))
                self.Chart_1.setGeometry(QtCore.QRect(100, 180, 341, 165))
            else:
                self.Chart_2.setGeometry(QtCore.QRect(460, 180, 356, 335))
                self.Chart_1.setGeometry(QtCore.QRect(100, 180, 356, 335))
        
            if ADI_count == 1:
                #self.Chart_3.show()
                print("랙이 너무 심해서 나중에 하겠슴다.")
            # self.Chart_box.show()
        print(f"chart_btn_Check : {chart_count}")

    def data_reset(self):

        global I_S
        global chart_count
        _translate = QtCore.QCoreApplication.translate
        if data_safe_count == 1:
            self.show_feedback("초기화 차단", "데이터 초기화가 차단되었습니다!")
        else:
            if safty_count == 1:
                self.show_feedback("Safty MODE", "안전 모드가 활성화 중입니다!")
                current_time_2 = datetime.now().strftime("%H:%M")
                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                self.feedback_Title.show()
                self.feedback_logo.show()
                self.feedback_Info.show()
                self.feedback_Box.show()
                self.feedback_time.show()
                QTest.qWait(3000)
                self.feedback_Title.hide()
                self.feedback_logo.hide()
                self.feedback_Info.hide()
                self.feedback_Box.hide()
                self.feedback_time.hide()
            else:
                I_S = 2
                chart_count = 0
                self.confirm_text1.setText(_translate("MainWindow", "데이터 초기화"))
                self.confirm_text2.setText(_translate("MainWindow", "데이터를 정말 초기화하시겠습니까?"))
                data_reset_img_path = Path(__file__).parent / "img" / "cauntion.png"
                self.confirm_logo.setPixmap(QtGui.QPixmap(str(data_reset_img_path)))
                self.confirm_btn1.show()
                self.confirm_btn2.show()
                self.confirm_box.show()
                self.confirm_logo.show()
                self.confirm_text2.show()
                self.confirm_exit_btn.show()
                self.confirm_text1.show()
                self.interface_box.hide()
                self.terminal_main.hide()
                self.Chart_1.hide()
                self.Chart_2.hide()
                #self.Chart_3.hide()

    def setting(self):
        _translate = QtCore.QCoreApplication.translate

        if set_mode_count == 0:
            if ADI_count == 1:
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(459, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(430, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "ON"))
                self.Chart_2.setGeometry(QtCore.QRect(100, 350, 341, 165))
                self.Chart_1.setGeometry(QtCore.QRect(100, 180, 341, 165))
                set_interface2_img = Path(__file__).parent / "img" / "settings" / "ADI_img.png"
                self.set_interface2_img.setPixmap(QtGui.QPixmap(str(set_interface2_img)))
            if ADI_count == 0:        
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(432, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(450, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "OFF"))
                self.Chart_2.setGeometry(QtCore.QRect(460, 180, 356, 335))
                self.Chart_1.setGeometry(QtCore.QRect(100, 180, 356, 335))
                set_interface2_img = Path(__file__).parent / "img" / "settings" / "ADI_img2.png"
                self.set_interface2_img.setPixmap(QtGui.QPixmap(str(set_interface2_img)))
            if VFS_count == 1:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
            if VFS_count == 0:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))

        global chart_count
        chart_count = 0
        self.settings_box1.show()
        self.Set_title.show()
        self.set_desc.show()
        self.settings_box2.show()
        self.settings_line.show()
        self.set_btn_box.show()
        self.safty_btn1.show()
        self.settings_exit_btn.show()
        self.sequence_btn1.show()
        self.advanced_btn1.show()
        self.data_btn1.show()
        self.interface_btn1.show()
        self.safty_btn2.show()
        self.sequence_btn2.show()
        self.data_btn2.show()
        self.advanced_btn2.show()
        self.interface_btn2.show()
        self.settings_text1_1.show()
        self.settings_text1_2.show()
        self.set_interface2_img_box.show()
        self.settings_text2_2.show()
        self.settings_text2_1.show()
        self.settings_btn1_1.show()
        self.settings_btn1_2.show()
        self.settings_btn1_3.show()
        self.set_a_btn2.show()
        self.set_a_btn3_2.show()
        #self.set_a_btn3.show()
        self.set_interface2_img.show()
        self.settings_text2_3.show()
        self.settings_btn2_1.show()
        self.settings_btn2_3.show()
        self.settings_btn2_2.show()
        self.programinfo_btn1.show()
        self.programinfo_btn2.show()
        self.settings_text3_2.show()
        self.settings_text3_1.show()
        self.set_interface3_Cbtn1.show()
        self.set_interface3_Cbtn2.show()
        self.checkBox_3.show()
        self.set_interface3_Cbtn3.show()
        #self.set_a_spinbox1.show()
        #self.set_a_spin1.show()

        self.terminal_main.hide()
        self.Chart_1.hide()
        self.Chart_2.hide()
        #self.Chart_3.hide()
        self.interface_box.hide()

    def gauge_interface_change(self):
        if set_mode_count == 0:
            if self.set_interface3_Cbtn1.isChecked():
                # 원형 게이지 UI 설정
                self.parameter1_box.setGeometry(QtCore.QRect(940, 540, 150, 150))
                self.parameter1_box.setStyleSheet(
                    "border-radius :75px;\n"
                    "font: 20pt \"AppleSDGothicNeoSB00\";\n"
                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,"
                    " stop:0 rgba(25, 25, 25, 150), stop:1 rgba(81, 81, 81, 100));")

                self.parameter2_box.setGeometry(QtCore.QRect(1100, 540, 150, 150))
                self.parameter2_box.setStyleSheet(
                    "border-radius :75px;\n"
                    "font: 20pt \"AppleSDGothicNeoSB00\";\n"
                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,"
                    " stop:0 rgba(25, 25, 25, 150), stop:1 rgba(81, 81, 81, 100));")

                self.parameter1_main.setStyleSheet(
                    "background-color: rgb(0, 0, 0, 0);\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 20pt \"Inter\";")
                self.parameter2_main.setStyleSheet(
                    "background-color: rgb(0, 0, 0, 0);\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 20pt \"Inter\";")

                self.parameter1_text1.setGeometry(QtCore.QRect(980, 580, 71, 20))
                self.parameter1_text2.setGeometry(QtCore.QRect(1000, 640, 31, 20))
                self.parameter1_main.setGeometry(QtCore.QRect(960, 600, 111, 41))

                self.parameter2_text1.setGeometry(QtCore.QRect(1140, 580, 71, 20))
                self.parameter2_text2.setGeometry(QtCore.QRect(1160, 640, 31, 20))
                self.parameter2_main.setGeometry(QtCore.QRect(1120, 600, 111, 41))

                self.gauge_r.show()
                self.gauge_b.show()

                self.parameter1_text1.show()
                self.parameter1_text2.show()
                self.parameter1_main.show()
                self.parameter1_box.show()
                self.parameter2_text1.show()
                self.parameter2_text2.show()
                self.parameter2_main.show()
                self.parameter2_box.show()

            elif self.set_interface3_Cbtn2.isChecked():
                # 사각 박스 게이지 UI 설정
                self.parameter1_main.setStyleSheet(
                    "background-color: rgb(0, 0, 0, 0);\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 17pt \"Inter\";")
                self.parameter2_main.setStyleSheet(
                    "background-color: rgb(0, 0, 0, 0);\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 17pt \"Inter\";")

                self.parameter1_box.setGeometry(QtCore.QRect(1020, 609, 111, 81))
                self.parameter2_box.setGeometry(QtCore.QRect(1140, 609, 111, 81))

                self.parameter1_text1.setGeometry(QtCore.QRect(1040, 620, 71, 20))
                self.parameter1_text2.setGeometry(QtCore.QRect(1060, 655, 31, 31))
                self.parameter1_main.setGeometry(QtCore.QRect(1020, 640, 111, 21))

                self.parameter2_text1.setGeometry(QtCore.QRect(1160, 620, 71, 20))
                self.parameter2_text2.setGeometry(QtCore.QRect(1180, 655, 31, 31))
                self.parameter2_main.setGeometry(QtCore.QRect(1140, 640, 111, 21))

                self.parameter1_box.setStyleSheet(
                    "border-radius :8px;\n"
                    "font: 20pt \"AppleSDGothicNeoSB00\";\n"
                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,"
                    " stop:0 rgba(25, 25, 25, 150), stop:1 rgba(81, 81, 81, 100));")
                self.parameter2_box.setStyleSheet(
                    "border-radius :8px;\n"
                    "font: 20pt \"AppleSDGothicNeoSB00\";\n"
                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,"
                    " stop:0 rgba(25, 25, 25, 150), stop:1 rgba(81, 81, 81, 100));")

                self.gauge_r.hide()
                self.gauge_b.hide()
                self.parameter1_text1.show()
                self.parameter1_text2.show()
                self.parameter1_main.show()
                self.parameter1_box.show()
                self.parameter2_text1.show()
                self.parameter2_text2.show()
                self.parameter2_main.show()
                self.parameter2_box.show()

            elif self.set_interface3_Cbtn3.isChecked():
                # 숨김 모드
                self.gauge_r.hide()
                self.gauge_b.hide()
                self.parameter1_text1.hide()
                self.parameter1_text2.hide()
                self.parameter1_main.hide()
                self.parameter1_box.hide()
                self.parameter2_text1.hide()
                self.parameter2_text2.hide()
                self.parameter2_main.hide()
                self.parameter2_box.hide()

    def set_interface(self):
        global set_mode_count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 0:
            set_mode_count = 0

        else:
            set_mode_count = 0
            self.Set_title.setText(_translate("MainWindow", "Interface"))
            self.set_desc.setText(_translate("MainWindow", "이곳에서 인터페이스 설정을 수정할 수 있습니다."))

            if VFS_count == 1:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
            if VFS_count == 0:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            self.settings_text1_1.setText(_translate("MainWindow", "VFS (Voice Feedback System) 활성화"))
            self.settings_text1_2.setText(_translate("MainWindow", "시스템 이벤트를 음성으로 안내하는 기능입니다."))


            if ADI_count == 1:
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(459, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(430, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "ON"))
            if ADI_count == 0:
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(432, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(450, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "OFF"))
            self.settings_text2_1.setText(_translate("MainWindow", "ADI (Attitude Direction Indicator) 활성화"))
            self.settings_text2_2.setText(_translate("MainWindow", "센서 데이터를 기반으로 실시간 회전 자세를 모니터 에서 확인할수 있습니다."))
            
            self.settings_btn1_1.show()
            self.settings_btn1_2.show()
            self.settings_btn1_3.show()
            self.settings_text1_1.show()
            self.settings_text1_2.show()
            self.settings_btn2_1.show()
            self.settings_btn2_2.show()
            self.settings_btn2_3.show()
            self.settings_text2_1.show()
            self.settings_text2_2.show()
            self.set_btn_box.setGeometry(QtCore.QRect(210, 60, 181, 41))
            self.settings_line.show()
            self.set_interface2_img.show()
            self.set_interface2_img_box.show()
            self.settings_text2_3.show()
            self.settings_text3_1.show()
            self.settings_text3_2.show()
            self.set_interface3_Cbtn1.show()
            self.set_interface3_Cbtn2.show()
            self.set_interface3_Cbtn3.show()
            self.set_a_btn3_2.show()
            self.set_a_btn2.show()

            self.Program_Info_Text2.hide()
            self.Program_Info_Logo.hide()
            self.Program_Info_Text1.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Box.hide()

    def set_advanced(self):
        global set_mode_count
        global detail_log_count
        global port_change_count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 1:
            set_mode_count = 1
        else:
            set_mode_count = 1
            self.Set_title.setText(_translate("MainWindow", "Advanced"))
            self.set_desc.setText(_translate("MainWindow", "이곳에서 고급 설정을 할 수 있습니다."))

            if detail_log_count == 1:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
            if detail_log_count == 0:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            self.settings_text1_1.setText(_translate("MainWindow", "시퀀스 디버그 로그 출력"))
            self.settings_text1_2.setText(_translate("MainWindow", "시퀀스 동작 로그를 상세하게 기록 할 수 있습니다."))

            self.settings_text2_1.setText(_translate("MainWindow", "기기(포트) 변경"))
            self.settings_text2_2.setText(_translate("MainWindow", "아래 연결 가능한 기기(포트) 목록을 확인한 후, 원하는 포트 번호를 입력해 주세요."))

            self.settings_btn2_1.hide()
            self.settings_btn2_2.hide()
            self.settings_btn2_3.hide()

            self.settings_btn1_1.show()
            self.settings_btn1_2.show()
            self.settings_btn1_3.show()
            self.settings_text1_1.show()
            self.settings_text1_2.show()
            self.settings_text2_1.show()
            self.settings_text2_2.show()

            self.set_btn_box.setGeometry(QtCore.QRect(210, 100, 181, 41))
            self.Program_Info_Text2.hide()
            self.Program_Info_Logo.hide()
            self.Program_Info_Text1.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Box.hide()
            self.set_interface2_img.hide()
            self.set_interface2_img_box.hide()
            self.settings_text2_3.hide()
            self.settings_text3_1.hide()
            self.settings_text3_2.hide()
            self.set_interface3_Cbtn1.hide()
            self.set_interface3_Cbtn2.hide()
            self.set_interface3_Cbtn3.hide()
            self.set_a_btn3_2.hide()
            self.set_a_btn2.hide()
            self.settings_line.show()

    def set_data(self):
        global set_mode_count
        global data_safe_count
        global simulation_data_count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 2:
            set_mode_count = 2
        else:
            set_mode_count = 2
            self.Set_title.setText(_translate("MainWindow", "Data"))
            self.set_desc.setText(_translate("MainWindow", "이곳에서 데이터 및 환경변수를 수정 할 수 있습니다."))

            if data_safe_count == 1:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
            if data_safe_count == 0:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            self.settings_text1_1.setText(_translate("MainWindow", "데이터 초기화 차단"))
            self.settings_text1_2.setText(_translate("MainWindow", "데이터 초기화를 무조건 차단합니다."))



            if simulation_data_count == 1:
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(459, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(430, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "ON"))
            if simulation_data_count == 0:
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(432, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(450, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "OFF"))
            self.settings_text2_1.setText(_translate("MainWindow", "Loop Time Display"))
            self.settings_text2_2.setText(_translate("MainWindow", "TMS 보드의 루프 주기를 실시간으로 표시합니다."))



            self.set_btn_box.setGeometry(QtCore.QRect(210, 140, 181, 41))

            self.settings_btn1_1.show()
            self.settings_btn1_2.show()
            self.settings_btn1_3.show()
            self.settings_text1_1.show()
            self.settings_text1_2.show()
            self.settings_btn2_1.show()
            self.settings_btn2_2.show()
            self.settings_btn2_3.show()
            self.settings_text2_1.show()
            self.settings_text2_2.show()
            
            self.Program_Info_Text2.hide()
            self.Program_Info_Logo.hide()
            self.Program_Info_Text1.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Box.hide()
            self.set_interface2_img.hide()
            self.set_interface2_img_box.hide()
            self.settings_text2_3.hide()
            self.settings_text3_1.hide()
            self.settings_text3_2.hide()
            self.set_interface3_Cbtn1.hide()
            self.set_interface3_Cbtn2.hide()
            self.set_interface3_Cbtn3.hide()
            self.set_a_btn3_2.hide()
            self.set_a_btn2.hide()

            self.settings_line.show()

    def set_sequence(self):
        global set_mode_count
        global sequence_manual_ig__count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 3:
            set_mode_count = 3
        else:
            set_mode_count = 3
            self.Set_title.setText(_translate("MainWindow", "Sequence"))
            self.set_desc.setText(_translate("MainWindow", "이곳에서 시퀀스를 설정 할 수 있습니다."))

            if sequence_manual_ig__count == 1:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
            if sequence_manual_ig__count == 0:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            self.settings_text1_1.setText(_translate("MainWindow", "시퀀스 내 수동점화"))
            self.settings_text1_2.setText(_translate("MainWindow", "T-0 도달 후 자동으로 점화하지 않고, 사용자가 최종 확인 후 직접 점화 버튼을 눌러 점화합니다."))

            self.settings_text2_1.setText(_translate("MainWindow", "시퀀스 타임"))  
            self.settings_text2_2.setText(_translate("MainWindow", "기본 시퀀스 타임을 1초 단위로 조정할수 있습니다."))

            self.set_btn_box.setGeometry(QtCore.QRect(210, 180, 181, 41))
            self.settings_btn1_1.show()
            self.settings_btn1_2.show()
            self.settings_btn1_3.show()
            self.settings_text1_1.show()
            self.settings_text1_2.show()
            self.settings_text2_1.show()
            self.settings_text2_2.show()
            
            self.Program_Info_Text2.hide()
            self.Program_Info_Logo.hide()
            self.Program_Info_Text1.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Box.hide()
            self.settings_btn2_1.hide()
            self.settings_btn2_2.hide()
            self.settings_btn2_3.hide()
            self.set_interface2_img.hide()
            self.set_interface2_img_box.hide()
            self.settings_text2_3.hide()
            self.settings_text3_1.hide()
            self.settings_text3_2.hide()
            self.set_interface3_Cbtn1.hide()
            self.set_interface3_Cbtn2.hide()
            self.set_interface3_Cbtn3.hide()
            self.set_a_btn3_2.hide()
            self.set_a_btn2.hide()
            self.settings_line.show()


    def set_safty(self):
        global set_mode_count
        global IFP_count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 4:
            set_mode_count = 4
        else:
            set_mode_count = 4
            self.Set_title.setText(_translate("MainWindow", "Safty"))
            self.set_desc.setText(_translate("MainWindow", "이곳에서 안전 관련 설정을 할 수 있습니다."))

            if IFP_count == 1:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
            if IFP_count == 0:
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            self.settings_text1_1.setText(_translate("MainWindow", "오작동 점화 차단 시스템 (IFP)"))
            self.settings_text1_2.setText(_translate("MainWindow", "의도치 않은 점화 신호가 들어왔을 경우, 물리적으로 즉시 차단하고 사용자 확인을 거치는 기능입니다."))

            self.set_btn_box.setGeometry(QtCore.QRect(210, 220, 181, 41))
            self.settings_btn1_1.show()
            self.settings_btn1_2.show()
            self.settings_btn1_3.show()
            self.settings_text1_1.show()
            self.settings_text1_2.show()

            self.Program_Info_Text2.hide()
            self.Program_Info_Logo.hide()
            self.Program_Info_Text1.hide()
            self.Program_Info_Text3.hide()
            self.Program_Info_Text4.hide()
            self.Program_Info_Text5.hide()
            self.Program_Info_Box.hide()
            self.settings_text2_1.hide()
            self.settings_text2_2.hide()
            self.settings_btn2_1.hide()
            self.settings_btn2_2.hide()
            self.settings_btn2_3.hide()
            self.set_interface2_img.hide()
            self.set_interface2_img_box.hide()
            self.settings_text2_3.hide()
            self.settings_text3_1.hide()
            self.settings_text3_2.hide()
            self.set_interface3_Cbtn1.hide()
            self.set_interface3_Cbtn2.hide()
            self.set_interface3_Cbtn3.hide()
            self.set_a_btn3_2.hide()
            self.set_a_btn2.hide()
            self.settings_line.show()
            self.settings_line.show()

    def set_info(self):
        global set_mode_count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 5:
            set_mode_count = 5
        else:
            set_mode_count = 5
            self.Set_title.setText(_translate("MainWindow", "Program info"))
            self.set_desc.setText(_translate("MainWindow", ""))
            self.Program_Info_Text1.show()
            self.Program_Info_Text2.show()
            self.Program_Info_Logo.show()
            self.Program_Info_Text3.show()
            self.Program_Info_Text4.show()
            self.Program_Info_Text5.show()
            self.Program_Info_Box.show()
            self.settings_line.hide()
            self.settings_text1_1.hide()
            self.settings_text1_2.hide()
            self.set_interface2_img_box.hide()
            self.settings_text2_2.hide()
            self.settings_text2_1.hide()
            self.settings_btn1_1.hide()
            self.settings_btn1_2.hide()
            self.settings_btn1_3.hide()
            self.set_a_btn2.hide()
            self.set_a_btn3_2.hide()
            self.set_a_btn3.hide()
            self.set_interface2_img.hide()
            self.settings_text2_3.hide()
            self.settings_btn2_1.hide()
            self.settings_btn2_3.hide()
            self.settings_btn2_2.hide()
            self.settings_text3_2.hide()
            self.settings_text3_1.hide()
            self.set_interface3_Cbtn1.hide()
            self.set_interface3_Cbtn2.hide()
            self.checkBox_3.hide()
            self.set_interface3_Cbtn3.hide()
            self.set_a_spinbox1.hide()
            self.set_a_spin1.hide()
            self.set_btn_box.setGeometry(QtCore.QRect(210, 260, 181, 41))

    def settings_btn1(self):
        global setting_interface_count
        global VFS_count
        global detail_log_count
        global data_safe_count
        global sequence_manual_ig__count
        global IFP_count
        _translate = QtCore.QCoreApplication.translate

        if set_mode_count == 0:
            if VFS_count == 1:
                VFS_count = 0
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            else:
                VFS_count = 1
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))

        if set_mode_count == 1:
            if detail_log_count == 1:
                detail_log_count = 0
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            else:
                detail_log_count = 1
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))

        if set_mode_count == 2:
            if data_safe_count == 1:
                data_safe_count = 0
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            else:
                data_safe_count = 1
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))

        if set_mode_count == 3:
            if sequence_manual_ig__count == 1:
                sequence_manual_ig__count = 0
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
            else:
                sequence_manual_ig__count = 1
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))

        if set_mode_count == 4:
            if IFP_count == 1:
                IFP_count = 0
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
                self.ser.write("IFP_OFF".encode())
            else:
                IFP_count = 1
                self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
                self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
                self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
                self.ser.write("IFP_ON".encode())

    def settings_btn2(self):
        global setting_interface_count
        global simulation_data_count
        global ADI_count
        _translate = QtCore.QCoreApplication.translate
        if set_mode_count == 0:
            if ADI_count == 1:
                ADI_count = 0
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(432, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(450, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "OFF"))
                self.Chart_2.setGeometry(QtCore.QRect(460, 180, 356, 335))
                self.Chart_1.setGeometry(QtCore.QRect(100, 180, 356, 335))
                set_interface2_img = Path(__file__).parent / "img" / "settings" / "ADI_img2.png"
                self.set_interface2_img.setPixmap(QtGui.QPixmap(str(set_interface2_img)))
            else:
                ADI_count = 1
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(459, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(430, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "ON"))
                self.Chart_2.setGeometry(QtCore.QRect(100, 350, 341, 165))
                self.Chart_1.setGeometry(QtCore.QRect(100, 180, 341, 165))
                set_interface2_img = Path(__file__).parent / "img" / "settings" / "ADI_img.png"
                self.set_interface2_img.setPixmap(QtGui.QPixmap(str(set_interface2_img)))
        if set_mode_count == 2:
            if simulation_data_count == 1:
                simulation_data_count = 0
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(432, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(450, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "OFF"))
            else:
                simulation_data_count = 1
                self.settings_btn2_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
                self.settings_btn2_3.setGeometry(QtCore.QRect(459, 282, 20, 17))
                self.settings_btn2_2.setGeometry(QtCore.QRect(430, 280, 31, 21))
                self.settings_btn2_2.setText(_translate("MainWindow", "ON"))


    def only_one_checked(self, state, source):
        if state == 2:
            for cb in [self.set_interface3_Cbtn1, self.set_interface3_Cbtn2, self.set_interface3_Cbtn3]:
                if cb is not source:
                    cb.blockSignals(True)
                    cb.setChecked(False)
                    cb.blockSignals(False)

    def settings_exit(self):
        global set_mode_count
        _translate = QtCore.QCoreApplication.translate

        if VFS_count == 1:
            self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(50,205,50);")
            self.settings_btn1_2.setGeometry(QtCore.QRect(459, 192, 20, 17))
            self.settings_btn1_3.setGeometry(QtCore.QRect(430, 190, 31, 21))
            self.settings_btn1_3.setText(_translate("MainWindow", "ON"))
        if VFS_count == 0:
            self.settings_btn1_1.setStyleSheet("border-radius :10px;\n" "background-color: rgb(145, 145, 145);")
            self.settings_btn1_2.setGeometry(QtCore.QRect(432, 192, 20, 17))
            self.settings_btn1_3.setGeometry(QtCore.QRect(450, 190, 31, 21))
            self.settings_btn1_3.setText(_translate("MainWindow", "OFF"))
        self.settings_text1_1.setText(_translate("MainWindow", "VFS (Voice Feedback System) 활성화"))
        self.settings_text1_2.setText(_translate("MainWindow", "시스템 이벤트를 음성으로 안내하는 기능입니다."))
        
        self.Set_title.setText(_translate("MainWindow", "Interface"))
        self.set_desc.setText(_translate("MainWindow", "이곳에서 인터페이스 설정을 수정할 수 있습니다."))
        
        self.set_btn_box.setGeometry(QtCore.QRect(210, 60, 181, 41))
        set_mode_count = 0
        self.Program_Info_Text2.hide()
        self.Program_Info_Logo.hide()
        self.Program_Info_Text1.hide()
        self.Program_Info_Text3.hide()
        self.Program_Info_Text4.hide()
        self.Program_Info_Text5.hide()
        self.Program_Info_Box.hide()
        self.settings_box1.hide()
        self.settings_exit_btn.hide()
        self.Set_title.hide()
        self.set_desc.hide()
        self.settings_box2.hide()
        self.set_btn_box.hide()
        self.safty_btn1.hide()
        self.settings_exit_btn.hide()
        self.settings_line.hide()
        self.sequence_btn1.hide()
        self.advanced_btn1.hide()
        self.data_btn1.hide()
        self.interface_btn1.hide()
        self.safty_btn2.hide()
        self.sequence_btn2.hide()
        self.data_btn2.hide()
        self.advanced_btn2.hide()
        self.interface_btn2.hide()
        self.settings_text1_1.hide()
        self.settings_text1_2.hide()
        self.set_interface2_img_box.hide()
        self.settings_text2_2.hide()
        self.settings_text2_1.hide()
        self.settings_btn1_1.hide()
        self.settings_btn1_2.hide()
        self.settings_btn1_3.hide()
        self.set_a_btn2.hide()
        self.set_a_btn3_2.hide()
        self.set_a_btn3.hide()
        self.set_interface2_img.hide()
        self.settings_text2_3.hide()
        self.settings_btn2_1.hide()
        self.settings_btn2_3.hide()
        self.settings_btn2_2.hide()
        self.programinfo_btn1.hide()
        self.programinfo_btn2.hide()
        self.settings_text3_2.hide()
        self.settings_text3_1.hide()
        self.set_interface3_Cbtn1.hide()
        self.set_interface3_Cbtn2.hide()
        self.checkBox_3.hide()
        self.set_interface3_Cbtn3.hide()
        self.set_a_spinbox1.hide()
        self.set_a_spin1.hide()






    def connecting(self):
        global simulation_mode
        _translate = QtCore.QCoreApplication.translate
        if simulation_mode == 1:
            self.intro_HW_main.setText(_translate("MainWindow", "기기 연결 없음"))
            simulation_img_path = Path(__file__).parent / "img" / "simulation.png"
            self.intro_HW_img.setPixmap(QtGui.QPixmap(str(simulation_img_path)))
            self.TimeUpdateThread = TimeUpdateThread()
            self.TimeUpdateThread.time_signal.connect(self.time)
            self.TimeUpdateThread.start()
        else:
            intro_img_path = Path(__file__).parent / "img" / "arduino_uno.png"
            self.intro_img.setPixmap(QtGui.QPixmap(str(intro_img_path)))

    def gauge(self, data):
        data_list = data.split(',')
        parameter1_data_g = float(data_list[0]) * 9.8  # 추력 (N)
        parameter2_data_g = float(data_list[1])        # 압력 (MPa)

        # 추력값이 0보다 작으면 인덱스 1
        if parameter1_data_g < 0:
            index_R = 1
        else:
            index_R = min(int(parameter1_data_g // 25) + 1, 20)

        # 압력값이 0보다 작으면 인덱스 1
        if parameter2_data_g < 0:
            index_B = 1
        else:
            index_B = min(round(parameter2_data_g / 0.3), 20)
            index_B = max(index_B, 1)  # 최소값 보장

        # 파일명 포맷: Gauge_R_01.png ~ Gauge_R_20.png
        filename_r = f"Gauge_R_{index_R:02d}.png"
        gauge_r_img = Path(__file__).parent / "img" / "gauge" / filename_r
        self.gauge_r.setPixmap(QtGui.QPixmap(str(gauge_r_img)))

        # 파일명 포맷: Gauge_B_01.png ~ Gauge_B_20.png
        filename_b = f"Gauge_B_{index_B:02d}.png"
        gauge_b_img = Path(__file__).parent / "img" / "gauge" / filename_b
        self.gauge_b.setPixmap(QtGui.QPixmap(str(gauge_b_img)))

    def signal_graph(self, data):

        global avg_parameter1_2
        global avg_parameter2_2
        global max_parameter1
        global max_parameter2

        chart1_pos = 0
        chart2_pos = 0

        if not hasattr(self, "frame_count"):
            self.frame_count = 0
        self.frame_count += 1
        if self.frame_count % 5 != 0:
            return  # 3 프레임 중 1번만 그래프 갱신

        try:
            data_list = data.split(',')
            parameter1_g_data = float(data_list[0]) * 9.8  # 추력 (N)
            parameter2_g_data = float(data_list[1])        # 압력 (Mpa)

            if not hasattr(self, "x_data"):
                self.x_data = []
                self.y_data = []
                self.y2_data = []
                self.start_time = time.time()

            if parameter1_g_data > 500 or parameter1_g_data < -100:
                print(f" 이상 센서 값 감지: {parameter1_g_data:.1f}N → 0N 처리됨")
                parameter1_g_data = 0
            elif parameter1_g_data < 0:
                parameter1_g_data = 0

            time_passed = time.time() - self.start_time
            self.x_data.append(time_passed)
            self.y_data.append(parameter1_g_data)
            self.y2_data.append(parameter2_g_data)

            self.Chart_1.clear()
            pen = pg.mkPen(color=(0, 200, 255), width=2)
            gradient = QtGui.QLinearGradient(0, 0, 0, 1000)
            gradient.setCoordinateMode(QtGui.QGradient.LogicalMode)
            gradient.setColorAt(1.0, QtGui.QColor(0, 200, 255, 250))
            gradient.setColorAt(0.0, QtGui.QColor(0, 200, 255, 0))
            brush = QtGui.QBrush(gradient)
            self.Chart_1.plot(self.x_data, self.y_data, pen=pen, fillLevel=0, brush=brush)

            self.Chart_2.clear()
            pen = pg.mkPen(color=(255, 24, 116), width=2)
            gradient = QtGui.QLinearGradient(0, 0, 0, 10)
            gradient.setCoordinateMode(QtGui.QGradient.LogicalMode)
            gradient.setColorAt(1.0, QtGui.QColor(216, 0, 68, 250))
            gradient.setColorAt(0.0, QtGui.QColor(216, 0, 68, 0))
            brush = QtGui.QBrush(gradient)
            self.Chart_2.plot(self.x_data, self.y2_data, pen=pen, fillLevel=0, brush=brush)

            for y in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]:
                self.Chart_1.addItem(pg.InfiniteLine(pos=y, angle=0, pen=pg.mkPen((150, 150, 150), width=0.3)))
            for y in [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]:
                self.Chart_2.addItem(pg.InfiniteLine(pos=y, angle=0, pen=pg.mkPen((150, 150, 150), width=0.3)))

            max_parameter1 = max(self.y_data)
            self.Chart_1.addItem(pg.InfiniteLine(pos=max_parameter1, angle=0, pen=pg.mkPen(color='red', width=1, style=pg.QtCore.Qt.DashLine)))

            parameter1_array = np.array(self.y_data)
            Effective_value1 = 10
            valid_indices = np.where(parameter1_array > Effective_value1)[0]
            if len(valid_indices) > 0:
                start_idx, end_idx = valid_indices[0], valid_indices[-1]
                avg_parameter1_2 = np.mean(parameter1_array[start_idx:end_idx + 1])
                self.Chart_1.addItem(pg.InfiniteLine(pos=avg_parameter1_2, angle=0, pen=pg.mkPen(color=QtGui.QColor(255, 179, 0), width=1, style=pg.QtCore.Qt.DashLine)))
                avg_text = pg.TextItem(text=f"평균값 (실제 값과 다를수 있음!)\n{avg_parameter1_2:.3f}", color=QtGui.QColor(255, 179, 0), anchor=(0, 0.5))
                avg_text.setPos(chart1_pos, avg_parameter1_2)
                self.Chart_1.addItem(avg_text)

            max_parameter2 = max(self.y2_data)
            self.Chart_2.addItem(pg.InfiniteLine(pos=max_parameter2, angle=0, pen=pg.mkPen(color='red', width=1, style=pg.QtCore.Qt.DashLine)))

            parameter2_array = np.array(self.y2_data)
            Effective_value2 = 1
            valid_indices = np.where(parameter2_array > Effective_value2)[0]
            if len(valid_indices) > 0:
                start_idx, end_idx = valid_indices[0], valid_indices[-1]
                avg_parameter2_2 = np.mean(parameter2_array[start_idx:end_idx + 1])
                self.Chart_2.addItem(pg.InfiniteLine(pos=avg_parameter2_2, angle=0, pen=pg.mkPen(color=QtGui.QColor(255, 179, 0), width=1, style=pg.QtCore.Qt.DashLine)))
                avg_text = pg.TextItem(text=f"평균값 (실제 값과 다를수 있음!)\n{avg_parameter2_2:.3f}", color=QtGui.QColor(255, 179, 0), anchor=(0, 0.5))
                avg_text.setPos(chart2_pos, avg_parameter2_2)
                self.Chart_2.addItem(avg_text)

            valid_indices = np.where(parameter1_array > Effective_value1)[0]
            if len(valid_indices) > 0:
                x_valid_start = self.x_data[valid_indices[0]]
                x_valid_end = self.x_data[valid_indices[-1]]
                chart1_pos = x_valid_end - (x_valid_end - x_valid_start) * 0.1

            valid_indices = np.where(parameter2_array > Effective_value2)[0]
            if len(valid_indices) > 0:
                x_valid_start = self.x_data[valid_indices[0]]
                x_valid_end = self.x_data[valid_indices[-1]]
                chart2_pos = x_valid_end - (x_valid_end - x_valid_start) * 0

            max_text = pg.TextItem(text=f"최대값 (실제 값과 다를수 있음!)\n{max_parameter1:.3f}", color=QtGui.QColor(216, 0, 68), anchor=(0, 0.5))
            max_text.setPos(chart1_pos, max_parameter1)
            self.Chart_1.addItem(max_text)

            max_text = pg.TextItem(text=f"최대값 (실제 값과 다를수 있음!)\n{max_parameter2:.3f}", color=QtGui.QColor(216, 0, 68), anchor=(0, 0.5))
            max_text.setPos(chart2_pos, max_parameter2)
            self.Chart_2.addItem(max_text)

        except Exception as e:
            print(f"signal 처리 중 오류: {e}")

    def hide_feedback(self):
        for widget in [self.feedback_Title, self.feedback_logo, self.feedback_Info, self.feedback_Box, self.feedback_time]:
            widget.hide()

    #하이드
    def show_feedback(self, title: str, info: str):
        _translate = QtCore.QCoreApplication.translate
        self.feedback_Title.setText(_translate("MainWindow", title))
        self.feedback_Info.setText(_translate("MainWindow", info))
        self.feedback_time.setText(_translate("MainWindow", datetime.now().strftime("%H:%M")))

        for widget in [self.feedback_Title, self.feedback_logo, self.feedback_Info, self.feedback_Box, self.feedback_time]:
            widget.show()

        if not hasattr(self, "feedback_timer"):
            self.feedback_timer = QTimer()
            self.feedback_timer.setSingleShot(True)
            self.feedback_timer.timeout.connect(self.hide_feedback)
        else:
            self.feedback_timer.stop()

        self.feedback_timer.start(3000)


    def signal(self, data):
        global IFP_confirm_popup_count
        global I_S
        global chart_count
        global IFP_count
        _translate = QtCore.QCoreApplication.translate

        def C_hide_feedback():
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
            self.flight_info_text.setText(_translate("MainWindow", "Normal"))

        def C_show_feedback(title, info, flight_status):
            self.flight_info_text.setText(_translate("MainWindow", flight_status))
            self.feedback_Title.setText(_translate("MainWindow", title))
            self.feedback_Info.setText(_translate("MainWindow", info))
            self.feedback_time.setText(_translate("MainWindow", datetime.now().strftime("%H:%M")))

            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()

            if not hasattr(self, "feedback_timer"):
                self.feedback_timer = QTimer()
                self.feedback_timer.setSingleShot(True)
                self.feedback_timer.timeout.connect(C_hide_feedback)
            else:
                self.feedback_timer.stop()
            self.feedback_timer.start(3000)
            
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        print(f"[{current_time}] Received data: {data}")
        self.flight_data_text.setText(f"[{current_time}]:{data}")
        self.log_entry += f"[{current_time}] Received data: {data}\n"
        self.terminal_main.append(f"[{current_time}]:{data}")

        try:
            data_list = data.split(',')
            parameter1_data = float(data_list[0]) * 9.8  # 추력 (N)
            parameter2_data = float(data_list[1])        # 압력 (Mpa)
            ignition_signal = int(data_list[5])
            ignition_signal2 = int(data_list[4])

            # 센서 이상값 처리
            if parameter1_data > 500:
                print(f"[{current_time}] 이상 센서 값 감지: {parameter1_data:.1f}N → 0N 처리됨")
                parameter1_data = 0
            elif parameter1_data < -100:
                print(f"[{current_time}] 이상 센서 값 감지: {parameter1_data:.1f}N → 0N 처리됨")
                parameter1_data = 0
            elif parameter1_data < 0:
                parameter1_data = 0

            self.parameter1_main.setText(_translate("MainWindow", f"{parameter1_data:.1f}"))
            self.parameter2_main.setText(_translate("MainWindow", f"{parameter2_data:.2f}"))
            

            if I_S == 0: # 수동 점화 상태
                # --- 점화 감지 ---

                if ignition_signal == 1 and not hasattr(self, 'ignition_detected'):
                    self.ignition_detected = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_2_3.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 점화 신호 감지")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255,140,0,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,140,0,70), stop:1 rgba(255, 255, 255, 0));")
                    self.show_feedback("점화", "점화 신호가 확인되었습니다!", "IGNITION 신호 확인")

                # --- 추진 시작 감지 ---
                if parameter1_data > 50 and not hasattr(self, 'thrust_detected'):
                    self.thrust_detected = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_2_4.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 유효 추력 감지됨: {parameter1_data:.1f}N")
                    self.show_feedback("추진 시작", "파라미터1 에서 유효값이 감지되었습니다!", "모터 상태: 추진 시작")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(220,20,60,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220,20,60,70), stop:1 rgba(255, 255, 255, 0));")

                # --- 추진 종료 감지 ---
                if hasattr(self, 'thrust_detected') and self.thrust_detected and not hasattr(self, 'thrust_ended') and parameter1_data < 20:
                    self.thrust_ended = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_2_5.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 추력 종료 감지됨: {parameter1_data:.1f}N")
                    self.show_feedback("추진 종료", "파라미터1 에서 유효값이 감지되지 않습니다!", "모터 상태: 추진 종료")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(30,144,255,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30,144,255,70), stop:1 rgba(255, 255, 255, 0));")

            if I_S == 1: # 시퀀스 상태
                # --- 점화 감지 ---
                if ignition_signal == 1 and not hasattr(self, 'ignition_detected'):
                    self.ignition_detected = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_1_3.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255,140,0,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,140,0,70), stop:1 rgba(255, 255, 255, 0));")
                    print(f"[{current_time}] ▶ 점화 신호 감지")
                    self.show_feedback("점화", "점화 신호가 확인되었습니다!", "IGNITION 신호 확인")
                    

                # --- 추진 시작 감지 ---
                if parameter1_data > 50 and not hasattr(self, 'thrust_detected'):
                    self.thrust_detected = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_1_4.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 유효 추력 감지됨: {parameter1_data:.1f}N")
                    self.show_feedback("추진 시작", "파라미터1 에서 유효값이 감지되었습니다!", "모터 상태: 추진 시작")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(220,20,60,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220,20,60,70), stop:1 rgba(255, 255, 255, 0));")

                # --- 추진 종료 감지 ---
                if hasattr(self, 'thrust_detected') and self.thrust_detected and not hasattr(self, 'thrust_ended') and parameter1_data < 20:
                    self.thrust_ended = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_1_5.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 추력 종료 감지됨: {parameter1_data:.1f}N")
                    self.show_feedback("추진 종료", "파라미터1 에서 유효값이 감지되지 않습니다!", "모터 상태: 추진 종료")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(30,144,255,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30,144,255,70), stop:1 rgba(255, 255, 255, 0));")
                    

            else: # 완전수동 점화 상태
                # --- 추진 시작 감지 ---
                if IFP_confirm_popup_count == 0:
                    if IFP_count == 1 and ignition_signal == 1:
                        IFP_confirm_popup_count = 1
                        I_S = 4
                        chart_count = 0
                        self.confirm_text1.setText(_translate("MainWindow", "예기치 않은 점화 신호 감지"))
                        self.confirm_text2.setText(_translate("MainWindow", "오작동 점화신호가 감지되어 차단하였습니다.\nIFP 를 해제 하시겠습니까?"))
                        sequence_ignition_img_path = Path(__file__).parent / "img" / "cauntion.png"
                        self.confirm_logo.setPixmap(QtGui.QPixmap(str(sequence_ignition_img_path)))
                        self.confirm_btn1.show()
                        self.confirm_btn2.show()
                        self.confirm_box.show()
                        self.confirm_logo.show()
                        self.confirm_text2.show()
                        self.confirm_exit_btn.show()
                        self.confirm_text1.show()
                        self.Chart_1.hide()
                        self.Chart_2.hide()
                        #self.Chart_3.hide()
                        self.interface_box.hide()
                        self.terminal_main.hide()
                        self.terminal_main.append("IFP 활성중! - CAUTION")
                        C_show_feedback("IFP 활성중!", "안전에 주의하세요!", "IFP 활성중! - CAUTION")
                
                if IFP_count == 0 and ignition_signal == 1:
                    self.terminal_main.append("점화신호 감지! - CAUTION")
                    C_show_feedback("점화신호 감지", "안전에 주의하세요!", "점화신호 감지! - CAUTION")

                if parameter1_data > 50 and not hasattr(self, 'thrust_detected'):
                    self.thrust_detected = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_3_4.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 유효 추력 감지됨: {parameter1_data:.1f}N")
                    self.show_feedback("추진 시작", "파라미터1 에서 유효값이 감지되었습니다!", "모터 상태: 추진 시작")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(220,20,60,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220,20,60,70), stop:1 rgba(255, 255, 255, 0));")

                # --- 추진 종료 감지 ---
                if hasattr(self, 'thrust_detected') and self.thrust_detected and not hasattr(self, 'thrust_ended') and parameter1_data < 20:
                    self.thrust_ended = True
                    step_img = Path(__file__).parent / "img" / "step" / "step_3_5.png"
                    self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                    print(f"[{current_time}] ▶ 추력 종료 감지됨: {parameter1_data:.1f}N")
                    self.show_feedback("추진 종료", "파라미터1 에서 유효값이 감지되지 않습니다!", "모터 상태: 추진 종료")
                    self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(30,144,255,70));")
                    self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30,144,255,70), stop:1 rgba(255, 255, 255, 0));")


        except Exception as e:
            print(f"[{current_time}] signal 처리 중 오류: {e}")


    def time(self, current_time):
        global sim_ig
        global t
        global intro_exit
        _translate = QtCore.QCoreApplication.translate
        self.Flight_interface_Time.setText(_translate("MainWindow", current_time))
        if intro_exit == 1:
            # 데이터 로깅 테스트 
            #self.log_entry += f"[{current_time}] Received data: test data\n"
            if sequence == 1:
                if simulation_mode == 0:
                    if abort == 0:
                        if t <= 0:
                            if t == 0:
                                self.flight_info_text.setText(_translate("MainWindow", "점화 신호 전송"))
                                self.ser.write("ignition".encode())
                            self.Abort_btn1.hide()
                            self.Abort_btn2.hide()
                            self.Abort_btn3.hide()
                            self.Abort_Box.hide()
                            self.Abort_text.hide()
                            self.Sequence_time_text.setText(_translate("Dialog", f"T+{-1*t}"))
                            t=t-1
                        else:
                            self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
                            t=t-1
                            if VFS_count == 1:
                                if t == 10:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "t minus.mp3")
                                    pygame.mixer.music.play()
                                    print("t_minus")
                                    self.terminal_main.append("t_minus")
                                elif t == 9:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "10.mp3")
                                    pygame.mixer.music.play()
                                    print("10")
                                    self.terminal_main.append("10")
                                if t == 8:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "9.mp3")
                                    pygame.mixer.music.play()
                                    print("9")
                                    self.terminal_main.append("9")
                                elif t == 7:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "8.mp3")
                                    pygame.mixer.music.play()
                                    print("8")
                                    self.terminal_main.append("8")
                                elif t == 6:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "7.mp3")
                                    pygame.mixer.music.play()
                                    print("7")
                                    self.terminal_main.append("7")
                                elif t == 5:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "6.mp3")
                                    pygame.mixer.music.play()
                                    print("6")
                                    self.terminal_main.append("6")
                                elif t == 4:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "5.mp3")
                                    pygame.mixer.music.play()
                                    print("5")
                                    self.terminal_main.append("5")
                                elif t == 3:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "4.mp3")
                                    pygame.mixer.music.play()
                                    print("4")
                                    self.terminal_main.append("4")
                                elif t == 2:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "3.mp3")
                                    pygame.mixer.music.play()
                                    print("3")
                                    self.terminal_main.append("3")
                                elif t == 1:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "2.mp3")
                                    pygame.mixer.music.play()
                                    print("2")
                                    self.terminal_main.append("2")
                                elif t == 0:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "1.mp3")
                                    pygame.mixer.music.play()
                                    print("1")
                                    self.terminal_main.append("1")

                else:
                    if abort == 0:
                        if t <= 0:
                            if t == 0:
                                def hide_feedback():
                                    self.feedback_Title.hide()
                                    self.feedback_logo.hide()
                                    self.feedback_Info.hide()
                                    self.feedback_Box.hide()
                                    self.feedback_time.hide()
                                    self.flight_info_text.setText(_translate("MainWindow", "Normal"))
                                pygame.mixer.music.load(Path(__file__).parent / "mp3" / "ignition.mp3")
                                pygame.mixer.music.play()
                                print("ignition")
                                self.terminal_main.append("ignition")
                                print("ignition_signal (가상)")
                                step_img = Path(__file__).parent / "img" / "step" / "step_1_3.png"
                                self.step.setPixmap(QtGui.QPixmap(str(step_img)))
                                self.flight_info_text.setText(_translate("MainWindow", "IGNITION (가상)"))
                                self.feedback_Title.setText(_translate("MainWindow", "점화"))
                                self.feedback_Info.setText(_translate("MainWindow", "점화 신호가 확인되었습니다! (가상)"))
                                self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255,140,0,70));")
                                self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,140,0,70), stop:1 rgba(255, 255, 255, 0));")
                                current_time_2 = datetime.now().strftime("%H:%M")
                                self.feedback_time.setText(_translate("MainWindow", current_time_2))
                                self.feedback_Title.show()
                                self.feedback_logo.show()
                                self.feedback_Info.show()
                                self.feedback_Box.show()
                                self.feedback_time.show()
                                QTimer.singleShot(3000, hide_feedback)
                            self.Abort_btn1.hide()
                            self.Abort_btn2.hide()
                            self.Abort_btn3.hide()
                            self.Abort_Box.hide()
                            self.Abort_text.hide()
                            self.Sequence_time_text.setText(_translate("Dialog", f"T+{-1*t}"))
                            t=t-1
                        else:
                            self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
                            t=t-1
                            if VFS_count == 1:
                                if t == 10:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "t minus.mp3")
                                    pygame.mixer.music.play()
                                    print("t_minus")
                                    self.terminal_main.append("t_minus")
                                elif t == 9:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "10.mp3")
                                    pygame.mixer.music.play()
                                    print("10")
                                    self.terminal_main.append("10")
                                if t == 8:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "9.mp3")
                                    pygame.mixer.music.play()
                                    print("9")
                                    self.terminal_main.append("9")
                                elif t == 7:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "8.mp3")
                                    pygame.mixer.music.play()
                                    print("8")
                                    self.terminal_main.append("8")
                                elif t == 6:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "7.mp3")
                                    pygame.mixer.music.play()
                                    print("7")
                                    self.terminal_main.append("7")
                                elif t == 5:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "6.mp3")
                                    pygame.mixer.music.play()
                                    print("6")
                                    self.terminal_main.append("6")
                                elif t == 4:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "5.mp3")
                                    pygame.mixer.music.play()
                                    print("5")
                                    self.terminal_main.append("5")
                                elif t == 3:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "4.mp3")
                                    pygame.mixer.music.play()
                                    print("4")
                                    self.terminal_main.append("4")
                                elif t == 2:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "3.mp3")
                                    pygame.mixer.music.play()
                                    print("3")
                                    self.terminal_main.append("3")
                                elif t == 1:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "2.mp3")
                                    pygame.mixer.music.play()
                                    print("2")
                                    self.terminal_main.append("2")
                                elif t == 0:
                                    pygame.mixer.music.load(Path(__file__).parent / "mp3" / "1.mp3")
                                    pygame.mixer.music.play()
                                    print("1")
                                    self.terminal_main.append("1")

    def LP_toggle(self):
        global I_S
        global chart_count
        _translate = QtCore.QCoreApplication.translate
        if safty_count == 1:
            self.show_feedback("Safty MODE", "안전 모드가 활성화 중입니다!")
        elif sequence == 1:
            self.show_feedback("주의", "시퀀스가 이미 진행중입니다!")
        else:
            I_S = 3
            chart_count = 0
            self.confirm_text1.setText(_translate("MainWindow", "발사대 자동 기립"))
            self.confirm_text2.setText(_translate("MainWindow", "발사대 자동 기립을 활성화 하시겠습니까?"))
            sequence_ignition_img_path = Path(__file__).parent / "img" / "LP_up.png"
            self.confirm_logo.setPixmap(QtGui.QPixmap(str(sequence_ignition_img_path)))
            self.confirm_btn1.show()
            self.confirm_btn2.show()
            self.confirm_box.show()
            self.confirm_logo.show()
            self.confirm_text2.show()
            self.confirm_exit_btn.show()
            self.confirm_text1.show()
            self.Chart_1.hide()
            self.Chart_2.hide()
            #self.Chart_3.hide()
            self.interface_box.hide()
            self.terminal_main.hide()


    def sequence(self):
        global I_S
        global chart_count
        _translate = QtCore.QCoreApplication.translate

        if sequence == 1:
            self.show_feedback("주의", "시퀀스가 이미 진행중입니다!")
        else:
            if safty_count == 1:
                self.show_feedback("Safty MODE", "안전 모드가 활성화 중입니다!")
            else:
                I_S = 1
                chart_count = 0
                self.confirm_text1.setText(_translate("MainWindow", "시퀀스 활성화"))
                self.confirm_text2.setText(_translate("MainWindow", "시퀀스를 활성화 하시겠습니까?"))
                sequence_ignition_img_path = Path(__file__).parent / "img" / "Sequence.png"
                self.confirm_logo.setPixmap(QtGui.QPixmap(str(sequence_ignition_img_path)))
                self.confirm_btn1.show()
                self.confirm_btn2.show()
                self.confirm_box.show()
                self.confirm_logo.show()
                self.confirm_text2.show()
                self.confirm_exit_btn.show()
                self.confirm_text1.show()
                self.Chart_1.hide()
                self.Chart_2.hide()
                #self.Chart_3.hide()
                self.interface_box.hide()
                self.terminal_main.hide()

    
    def confirm_exit(self):
        global IFP_confirm_popup_count
        self.confirm_btn1.hide()
        self.confirm_btn2.hide()
        self.confirm_box.hide()
        self.confirm_logo.hide()
        self.confirm_text2.hide()
        self.confirm_exit_btn.hide()
        self.confirm_text1.hide()
        IFP_confirm_popup_count = 0

    def HW_Check(self):
        # self.x_data = []
        # self.y_data = []
        # self.y2_data = []
        
        # # 가상 데이터 생성
        # # 비어있던 데이터에 가상 데이터를 할당
        # self.x_data = np.linspace(0, 5, 1000)
        # self.y_data = np.piecewise(
        #     self.x_data,
        #     [self.x_data < 0.2, (0.2 <= self.x_data) & (self.x_data < 3.5), self.x_data >= 3.5],
        #     [
        #         lambda x: 500 * (x / 0.2),         # 급상승 (점화 구간)
        #         lambda x: 500,                     # 유지 구간
        #         lambda x: 500 * np.exp(-5*(x - 3.5))  # 연소 종료 감쇠
        #     ]
        # )
        # self.y2_data = np.piecewise(
        #     self.x_data,
        #     [self.x_data < 0.2, (0.2 <= self.x_data) & (self.x_data < 3.5), self.x_data >= 3.5],
        #     [
        #         lambda x: 4 * (x / 0.2),         # 급상승 (점화 구간)
        #         lambda x: 4,                     # 유지 구간
        #         lambda x: 4 * np.exp(-5*(x - 3.5))  # 연소 종료 감쇠
        #     ]
        # )    

        # # 그래프 클리어 후 그리기
        # self.Chart_1.clear()
        # self.Chart_1.plot(self.x_data, self.y_data)

        
        
        # pen = pg.mkPen(color=(0, 200, 255), width=2)

        # gradient = QtGui.QLinearGradient(0, 0, 0, 1000)  # y=0 ~ y=10 구간에서 그라데이션
        # gradient.setCoordinateMode(QtGui.QGradient.LogicalMode)
        # gradient.setColorAt(1.0, QtGui.QColor(0, 200, 255, 200))    # 위쪽
        # gradient.setColorAt(0.0, QtGui.QColor(0, 200, 255, 0))  # 아래쪽

        # brush = QtGui.QBrush(gradient)



        # self.Chart_1.plot(
        #     self.x_data, self.y_data,
        #     pen=pen,
        #     fillLevel=0,        # y=0을 기준으로 아래를 채움
        #     brush=brush         # 채우는 색
        # )

        # # 압력 그래프 (Chart_2)
        # self.Chart_2.clear()
        # self.Chart_2.plot(self.x_data, self.y2_data)

        # pen = pg.mkPen(color=(255, 24, 116), width=2)

        # gradient = QtGui.QLinearGradient(0, 0, 0, 10)  # y=0 ~ y=10 구간에서 그라데이션
        # gradient.setCoordinateMode(QtGui.QGradient.LogicalMode)
        # gradient.setColorAt(1.0, QtGui.QColor(216, 0, 68, 200))    # 위쪽rgb(216, 0, 68)  QtGui.QColor(216, 0, 68) QtGui.QColor(0, 200, 255
        # gradient.setColorAt(0.0, QtGui.QColor(216, 0, 68, 0))  # 아래쪽

        # brush = QtGui.QBrush(gradient)
        
        # self.Chart_2.plot(
        #     self.x_data, self.y2_data,
        #     pen=pen,
        #     fillLevel=0,        # y=0을 기준으로 아래를 채움
        #     brush=brush         # 채우는 색
        # )
        # for y_value in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]:
        #     line = pg.InfiniteLine(pos=y_value, angle=0, pen=pg.mkPen((150, 150, 150), width=0.3))
        #     self.Chart_1.addItem(line)
        # for y_value in [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]:
        #     line = pg.InfiniteLine(pos=y_value, angle=0, pen=pg.mkPen((150, 150, 150), width=0.3))
        #     self.Chart_2.addItem(line)

        # # 최대 파라미터1 계산
        # max_parameter1 = max(self.y_data)

        # # 최대 파라미터1 지점에 빨간 가로줄 추가
        # max_line = pg.InfiniteLine(
        #     pos=max_parameter1,
        #     angle=0,  # 수평선
        #     pen=pg.mkPen(color='red', width=1, style=pg.QtCore.Qt.DashLine)
        # )
        # self.Chart_1.addItem(max_line)

        # # 평균 파라미터1 계산
        # avg_parameter1 = sum(self.y_data) / len(self.y_data)

        # # 평균 파라미터1 지점에 파란 점선 추가
        # avg_line = pg.InfiniteLine(
        #     pos=avg_parameter1,
        #     angle=0,  # 수평선
        #     pen=pg.mkPen(color=QtGui.QColor(255, 179, 0), width=1, style=pg.QtCore.Qt.DashLine)
        # )
        # self.Chart_1.addItem(avg_line)

        #  # 최대 파라미터2 계산
        # max_parameter2 = max(self.y2_data)

        # # 최대 파라미터2 지점에 빨간 가로줄 추가
        # max_line = pg.InfiniteLine(
        #     pos=max_parameter2,
        #     angle=0,  # 수평선
        #     pen=pg.mkPen(color='red', width=1, style=pg.QtCore.Qt.DashLine)
        # )
        # self.Chart_2.addItem(max_line)

        # # 평균 파라미터2 계산
        # avg_parameter2 = sum(self.y2_data) / len(self.y2_data)

        # # 평균 파라미터2 지점에 파란 점선 추가
        # avg_line = pg.InfiniteLine(
        #     pos=avg_parameter2,
        #     angle=0,  # 수평선
        #     pen=pg.mkPen(color=QtGui.QColor(255, 179, 0), width=1, style=pg.QtCore.Qt.DashLine)
        # )
        # self.Chart_2.addItem(avg_line)

        # parameter1_array = np.array(self.y_data)
        # Effective_value1 = 10  # 데이터10 이상을 유효 구간으로 간주

        # # 유효 추력 시작/끝 인덱스 구하기
        # valid_indices = np.where(parameter1_array > Effective_value1)[0]
        # if len(valid_indices) > 0:
        #     start_idx = valid_indices[0]
        #     end_idx = valid_indices[-1]
        #     x_valid_start = self.x_data[start_idx]
        #     x_valid_end = self.x_data[end_idx]

        #     # 평균, 최대값 좌표도 유효 구간에 맞춰 텍스트 배치
        #     chart1_pos = x_valid_end - (x_valid_end - x_valid_start) * 0.1  # 유효 구간 끝에서 10% 안쪽

        # parameter2_array = np.array(self.y2_data)
        # Effective_value2 = 1  # 데이터 1 이상을 유효 구간으로 간주

        # # 유효 추력 시작/끝 인덱스 구하기
        # valid_indices = np.where(parameter2_array > Effective_value2)[0]
        # if len(valid_indices) > 0:
        #     start_idx = valid_indices[0]
        #     end_idx = valid_indices[-1]
        #     x_valid_start = self.x_data[start_idx]
        #     x_valid_end = self.x_data[end_idx]

        #     # 평균, 최대값 좌표도 유효 구간에 맞춰 텍스트 배치
        #     chart2_pos = x_valid_end - (x_valid_end - x_valid_start) * 0  # 유효 구간 끝에서 10% 안쪽



        # # 텍스트 아이템 추가: 최대 파라미터1값
        # max_text = pg.TextItem(text=f"최대값 (실제 값과 다를수 있음!)\n{max_parameter1:.3f}", color=QtGui.QColor(216, 0, 68), anchor=(0, 0.5))
        # max_text.setPos(chart1_pos, max_parameter1)
        # self.Chart_1.addItem(max_text)

        # # 텍스트 아이템 추가: 평균 파라미터1값
        # avg_text = pg.TextItem(text=f"평균값 (실제 값과 다를수 있음!)\n{avg_parameter1:.3f}", color=QtGui.QColor(255, 179, 0), anchor=(0, 0.5))
        # avg_text.setPos(chart1_pos, avg_parameter1)
        # self.Chart_1.addItem(avg_text)

        # # 텍스트 아이템 추가: 최대 파라미터2값
        # max_text = pg.TextItem(text=f"최대값 (실제 값과 다를수 있음!)\n{max_parameter2:.3f}", color=QtGui.QColor(216, 0, 68), anchor=(0, 0.5))
        # max_text.setPos(chart2_pos, max_parameter2)
        # self.Chart_2.addItem(max_text)

        # # 텍스트 아이템 추가: 평균 파라미터2값
        # avg_text = pg.TextItem(text=f"평균값 (실제 값과 다를수 있음!)\n{avg_parameter2:.3f}", color=QtGui.QColor(255, 179, 0), anchor=(0, 0.5))
        # avg_text.setPos(chart2_pos, avg_parameter2)
        # self.Chart_2.addItem(avg_text)
        print("HWcheck")
        
    def Manual_Ignition(self):
        global I_S
        global chart_count
        I_S = 0
        _translate = QtCore.QCoreApplication.translate

        if safty_count == 1:
            self.show_feedback("Safty MODE", "안전 모드가 활성화 중입니다!")
        elif sequence == 1:
            self.show_feedback("주의", "시퀀스가 이미 진행중입니다!")
        else:
            chart_count = 0
            print("Manual_Ignition")
            self.confirm_text1.setText(_translate("MainWindow", "수동 점화"))
            self.confirm_text2.setText(_translate("MainWindow", "수동 점화를 활성화 하시겠습니까?"))
            manual_ignition_img_path = Path(__file__).parent / "img" / "cauntion.png"
            self.confirm_logo.setPixmap(QtGui.QPixmap(str(manual_ignition_img_path)))
            self.confirm_btn1.show()
            self.confirm_btn2.show()
            self.confirm_box.show()
            self.confirm_logo.show()
            self.confirm_text2.show()
            self.confirm_exit_btn.show()
            self.confirm_text1.show()
            self.Chart_1.hide()
            self.Chart_2.hide()
            #self.Chart_3.hide()
            self.interface_box.hide()
            self.terminal_main.hide()


    def seq_reset(self):
        global t
        global t_set
        global I_S
        global sequence
        global re_seq_count

        _translate = QtCore.QCoreApplication.translate

        if sequence == 1:
            I_S = 5
            sequence = 0
            t = t_set
            self.Abort_btn1.hide()
            self.Abort_btn2.hide()
            self.Abort_btn3.hide()
            self.Abort_Box.hide()
            self.Abort_text.hide()
            step_img = Path(__file__).parent / "img" / "step" / "step_1_1.png"
            self.step.setPixmap(QtGui.QPixmap(str(step_img)))
            # 시퀀스 시간 초기화
            self.Sequence_time_text.setText(_translate("Dialog", f"T-{t_set}"))
            self.show_feedback("시퀀스 초기화", "시퀀스가 초기화되었습니다!")
            self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(0,0,0,150));")
            self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,0,0,150), stop:1 rgba(255, 255, 255, 0));")
        else:
            self.show_feedback("시퀀스 거부", "시퀀스가 작동중이지 않습니다!")

    def seq_tp10(self):
        global t
        global t_set
        global I_S
        global sequence
        global re_seq_count

        _translate = QtCore.QCoreApplication.translate


        if sequence == 1:
            if t > 0:
                t += 10
                self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
                self.show_feedback("시퀀스 메니저", "시퀀스를 연장하였습니다!")
            else:
                self.show_feedback("시퀀스 메니저", "시퀀스가 이미 t- 입니다!")
        else:
            t_set += 10
            t = t_set
            self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
            self.show_feedback("시퀀스 메니저", "시퀀스를 연장하였습니다!")

    def seq_tm10(self):
        global t
        global t_set
        global I_S
        global sequence
        global re_seq_count

        _translate = QtCore.QCoreApplication.translate

        if sequence == 1:
            if t > 0:
                if t > 20:
                    t -= 10
                    self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
                    self.show_feedback("시퀀스 메니저", "시퀀스를 단축하였습니다!")
                else:
                    self.show_feedback("시퀀스 메니저", "시퀀스가 t-20 이하 입니다!")
            else:
                self.show_feedback("시퀀스 메니저", "시퀀스가 이미 t- 입니다!")
        else:
            if t_set > 20:
                t_set -= 10
                t = t_set
                self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
                self.show_feedback("시퀀스 메니저", "시퀀스를 단축하였습니다!")
            else:
                self.show_feedback("시퀀스 메니저", "시퀀스가 t-20 이하 입니다!")


    def LP_stop(self):

        global safty_count

        _translate = QtCore.QCoreApplication.translate

        def C_hide_feedback():
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
            self.flight_info_text.setText(_translate("MainWindow", "Normal"))

        def C_show_feedback(title, info, flight_status):
            self.flight_info_text.setText(_translate("MainWindow", flight_status))
            self.feedback_Title.setText(_translate("MainWindow", title))
            self.feedback_Info.setText(_translate("MainWindow", info))
            self.feedback_time.setText(_translate("MainWindow", datetime.now().strftime("%H:%M")))

            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()

            if not hasattr(self, "feedback_timer"):
                self.feedback_timer = QTimer()
                self.feedback_timer.setSingleShot(True)
                self.feedback_timer.timeout.connect(C_hide_feedback)
            else:
                self.feedback_timer.stop()
            self.feedback_timer.start(3000)

        self.LP_exit_btn.hide()
        self.LP_level_img.hide()
        self.LP_text1.hide()
        self.LP_text2.hide()
        self.confirm_box.hide()

        safty_count = 1
        
        # 안전모드 이미지 전환
        safty_img_path = Path(__file__).parent / "img" / "safty_locked.png"
        self.Flight_interface_Safty_btn.setPixmap(QtGui.QPixmap(str(safty_img_path)))

        # ABORT 피드백 출력
        C_show_feedback("발사대 기립 중단", "안전모드로 자동 변환 되었습니다!", "발사대 기립 중단 - 사용자에 의해 중단되었습니다!")

        self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(220,20,60,70));")
        self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220,20,60,70), stop:1 rgba(255, 255, 255, 0));")
        

    def abort(self):
        global sequence
        global abort
        global t_set
        global safty_count

        _translate = QtCore.QCoreApplication.translate

        def C_hide_feedback():
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
            self.flight_info_text.setText(_translate("MainWindow", "Normal"))

        def C_show_feedback(title, info, flight_status):
            self.flight_info_text.setText(_translate("MainWindow", flight_status))
            self.feedback_Title.setText(_translate("MainWindow", title))
            self.feedback_Info.setText(_translate("MainWindow", info))
            self.feedback_time.setText(_translate("MainWindow", datetime.now().strftime("%H:%M")))

            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()

            if not hasattr(self, "feedback_timer"):
                self.feedback_timer = QTimer()
                self.feedback_timer.setSingleShot(True)
                self.feedback_timer.timeout.connect(C_hide_feedback)
            else:
                self.feedback_timer.stop()
            self.feedback_timer.start(3000)

        sequence = 0
        abort = 0
        safty_count = 1


        step_img = Path(__file__).parent / "img" / "step" / "step_1_1.png"
        self.step.setPixmap(QtGui.QPixmap(str(step_img)))

        if VFS_count == 1:
            # 음성 출력
            pygame.mixer.music.stop()
            pygame.mixer.music.load(Path(__file__).parent / "mp3" / "abort.mp3")
            pygame.mixer.music.play()
            print("play")

        # 시퀀스 시간 초기화
        self.Sequence_time_text.setText(_translate("Dialog", f"T-{t_set}"))
        

        # 안전모드 이미지 전환
        safty_img_path = Path(__file__).parent / "img" / "safty_locked.png"
        self.Flight_interface_Safty_btn.setPixmap(QtGui.QPixmap(str(safty_img_path)))

        # ABORT UI 숨기기
        self.Abort_btn1.hide()
        self.Abort_btn2.hide()
        self.Abort_btn3.hide()
        self.Abort_Box.hide()
        self.Abort_text.hide()
        

        # ABORT 피드백 출력
        C_show_feedback("ABORT", "안전모드로 자동 변환 되었습니다!", "ABORT - 시퀀스가 중단되었습니다!")

        self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(220,20,60,70));")
        self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220,20,60,70), stop:1 rgba(255, 255, 255, 0));")

    def Confirm(self):
        _translate = QtCore.QCoreApplication.translate
        global I_S
        global t
        global t_set
        global sequence

        global IFP_count
        global IFP_confirm_popup_count
        global avg_parameter1_2
        global avg_parameter2_2
        global max_parameter1
        global max_parameter2

        def C_hide_feedback():
            self.feedback_Title.hide()
            self.feedback_logo.hide()
            self.feedback_Info.hide()
            self.feedback_Box.hide()
            self.feedback_time.hide()
            self.flight_info_text.setText(_translate("MainWindow", "Normal"))

        def C_show_feedback(title, info, flight_status):
            self.flight_info_text.setText(_translate("MainWindow", flight_status))
            self.feedback_Title.setText(_translate("MainWindow", title))
            self.feedback_Info.setText(_translate("MainWindow", info))
            self.feedback_time.setText(_translate("MainWindow", datetime.now().strftime("%H:%M")))

            self.feedback_Title.show()
            self.feedback_logo.show()
            self.feedback_Info.show()
            self.feedback_Box.show()
            self.feedback_time.show()

            if not hasattr(self, "feedback_timer"):
                self.feedback_timer = QTimer()
                self.feedback_timer.setSingleShot(True)
                self.feedback_timer.timeout.connect(C_hide_feedback)
            else:
                self.feedback_timer.stop()
            self.feedback_timer.start(3000)

        # UI 숨기기 (공통)
        self.confirm_btn1.hide()
        self.confirm_btn2.hide()
        self.confirm_logo.hide()
        self.confirm_text2.hide()
        self.confirm_exit_btn.hide()
        self.confirm_text1.hide()

        if I_S == 0:  # 수동 점화
            self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255,140,70));")
            self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,140,70), stop:1 rgba(255, 255, 255, 0));")
            pygame.mixer.music.load(Path(__file__).parent / "mp3" / "ignition.mp3")
            pygame.mixer.music.play()
            print("ignition")
            self.terminal_main.append("ignition")
            self.ser.write("ignition".encode())
            C_show_feedback("수동 점화", "수동 점화가 시작되었습니다!", "수동 점화 시작")
            self.confirm_box.hide()

        if I_S == 1: # 시퀀스 시작
            t = t_set
            step_img = Path(__file__).parent / "img" / "step" / "step_1.png"
            self.step.setPixmap(QtGui.QPixmap(str(step_img)))
            print("sequence")
            sequence = 1
            self.flight_info_text.setText(_translate("MainWindow", "카운트다운 시작"))
            self.Abort_btn1.show()
            self.Abort_btn2.show()
            self.Abort_btn3.show()
            self.Abort_Box.show()
            self.Abort_text.show()
            self.Sequence_time_text.setText(_translate("Dialog", f"T-{t}"))
            step_img = Path(__file__).parent / "img" / "step" / "step_1_2.png"
            self.step.setPixmap(QtGui.QPixmap(str(step_img)))
            self.confirm_box.hide()

            C_show_feedback("시퀀스 허가", "시퀀스가 시작되었습니다!", "카운트다운 시작")

            self.back_grad_down.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(30,144,255,70));")
            self.back_grad_up.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30,144,255,70), stop:1 rgba(255, 255, 255, 0));")


        if I_S == 2:  # 데이터 초기화
            print("data_reset")
            self.terminal_main.append("data_reset")
            self.log_entry = ""
            self.x_data = []
            self.y_data = []
            self.y2_data = []
            avg_parameter1_2 = 0
            avg_parameter2_2 = 0
            max_parameter1 = 00
            max_parameter2 = 0

            self.confirm_box.hide()

            print("▶ 로그 및 그래프 데이터 초기화 완료")
            print(f"log_entry: '{self.log_entry}'")
            print(f"x_data: {self.x_data}")
            print(f"y_data: {self.y_data}")
            print(f"y2_data: {self.y2_data}")
            print(f"avg_parameter1_2: {avg_parameter1_2}")
            print(f"avg_parameter2_2: {avg_parameter2_2}")
            print(f"max_parameter1: {max_parameter1}")
            print(f"max_parameter2: {max_parameter2}")

            self.terminal_main.append("※ 로그 및 그래프 데이터가 초기화되었습니다.")
            self.terminal_main.append(f"avg_parameter1_2 = {avg_parameter1_2}")
            self.terminal_main.append(f"avg_parameter2_2 = {avg_parameter2_2}")
            self.terminal_main.append(f"max_parameter1 = {max_parameter1}")
            self.terminal_main.append(f"max_parameter2 = {max_parameter2}")

            self.start_time = time.time()
            self.Chart_1.clear()
            C_show_feedback("데이터 초기화 완료! ", "초기화 후에도 로그는 터미널에 보존됩니다.","Data reset")

        if I_S == 3: # 발사대 기립
            print("lp")
            self.LP_level_img.show()
            self.LP_text1.show()
            self.LP_text2.show()
            self.LP_exit_btn.show()

        if I_S == 4: #IFP 모드
            IFP_count = 0
            IFP_confirm_popup_count = 0
            self.confirm_box.hide()
            self.ser.write("IFP_OFF".encode())



    def export(self):


        _translate = QtCore.QCoreApplication.translate
        print("export")
        self.log_entry += "--------------------------------------------------------\n"
        self.log_entry += "- End of Data - "

        # 로그 파일 경로 설정
        log_dir = Path(__file__).parent / "LOG"
        
        # 디렉토리가 없는 경우 생성
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 파일 이름을 현재 시간으로 설정
        current_time_for_filename = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file_name = f"serial_log_{current_time_for_filename}.txt"
        log_file_path = os.path.join(log_dir, log_file_name)
        
        # log_entry에 저장된 로그 메시지를 파일에 추가 기록
        with open(log_file_path, "a") as log_file:
            log_file.write(self.log_entry)

        # 로그 저장 후 콘솔 출력
        print(f"Log saved in: {log_file_path}")
        print(self.log_entry.strip())
        # 피드백 출력
        self.show_feedback("Export", "로그를 .txt 파일로 변환하였습니다")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.connecting()
    sys.exit(app.exec_())
