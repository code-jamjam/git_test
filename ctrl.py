from PyQt5.QtWidgets import QMessageBox

class control:
    def __init__(self, view):
        self.view = view
        self.connectSignal()


    def connectSignal(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
