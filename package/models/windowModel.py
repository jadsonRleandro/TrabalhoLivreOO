import sys
from PyQt6.QtWidgets import * 


class window:
    def __init__(self, height, width, tittle):
        self.height = height
        self.width = width
        self.title = tittle

class Gui(window):
    def __init__(self,height, width, tittle):
        super().__init__(height, width, tittle)
        self.app = QApplication(sys.argv)
        self.gui = QWidget()
        self.gui.setStyleSheet("background-color: 'black';")
        self.gui.setWindowTitle(self.title)
        
    def exe(self):
        


        self.show()
        self.app.exec()
    def modify():
        pass

    def show(self):
        self.gui.resize(self.height, self.width)
        self.gui.show()

    def exit(self):
        self.gui.close()

class label():
    def __init__(self, txt = "", window = None, x = 0, y = 0, style = ""):
        self.text = QLabel(txt, window)
        self.text.move(x, y)
        self.text.setStyleSheet(style)
    
    def modifyTxt(self,newtxt, x, y):
        self.text.setText(newtxt)
        self.text.resize(x, y)

class inp():
    def __init__(self, txt = "", window = None, x = 0, y = 0, style = "", height = 0, width = 0):
        self.inpt = QLineEdit(txt, window)
        self.inpt.setGeometry(x,y,height,width)
        self.inpt.setStyleSheet(style)

class btn():
        def __init__(self, txt = "", window = None, x = 0, y = 0, style = "", height = 0, width = 0):
            self.button = QPushButton(txt, window)
            self.button.setGeometry(x,y,height,width)
            self.button.setStyleSheet(style)

        def pressBtn(self, func):
            self.button.clicked.connect(func)