import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox

def initUI(self):
    # 클래스 선언
    class View(QWidget) :
        # 생성자 함수
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 윈도우 버튼 생성
            self.btn1 = QPushButton('Message', self)

        # 버튼의 위치를 수정
            # 수직 레이아웃 위젯 생성
            vbox = QVBoxLayout()
            # 비어있는 공간을 생성
            vbox.addStretch(1)
            # 버튼을 추가
            vbox.addWidget(self.btn1)
            # 비어있는 공간을 생성
            vbox.addStretch(1)
            # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 생성
            self.setLayout(vbox)

            self.setWindowTitle("Calculator") # 새로운 화면에 제목
            self.resize(256, 256) # 새로운 화면의 사이즈
            self.show() # 윈도우 화면을 출력

        # 버튼 클릭시 실행할 이벤트 함수를 생성
        def activateMessage(self):
            # 버튼 클릭 시 메시지 박스 출력
            QMessageBox.information(self, "information", 'Button clicked!')


    # if __name__=="__main__":
    #     app = QApplication(sys.argv) # 클래스 생성
    #     view = Calculator() # 클래스 생성
    #     sys.exit(app.exec_()) # 애플리케이션에서 이벤트를 처리하는 루프 생성