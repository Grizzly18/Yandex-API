import sys
from main import get_picture
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from design import Ui_MainWindow

# .\prog.py Москва, ул. Ак. Королева, 12

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self, address):
        super().__init__()
        self.mspn = 0
        self.mll = [0, 0]
        self.setupUi(self)
        self.setWindowTitle("Большая задача по Maps API. Часть №3")
        self.map_file = "map.png"
        self.PgUp.clicked.connect(self.PgUpFunc)
        self.PgDown.clicked.connect(self.PgDownFunc)
        self.Up.clicked.connect(self.UpFunc)
        self.Down.clicked.connect(self.DownFunc)
        self.Left.clicked.connect(self.LeftFunc)
        self.Right.clicked.connect(self.RightFunc)
        self.pict = get_picture(address, with_label=True)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def LeftFunc(self):
        self.mll[0] -= 0.001
        self.pict = get_picture(address, True, self.mspn, self.mll)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def RightFunc(self):
        self.mll[0] += 0.001
        self.pict = get_picture(address, True, self.mspn, self.mll)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def UpFunc(self):
        self.mll[1] += 0.001
        self.pict = get_picture(address, True, self.mspn, self.mll)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def DownFunc(self):
        self.mll[1] -= 0.001
        self.pict = get_picture(address, True, self.mspn, self.mll)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def PgUpFunc(self):
        self.mspn += 0.001
        self.pict = get_picture(address, True, self.mspn)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)


    def PgDownFunc(self):
        self.mspn -= 0.001
        self.pict = get_picture(address, True, self.mspn)
        with open(self.map_file, "wb") as file:
            file.write(self.pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)



if __name__ == '__main__':
    address = " ".join(sys.argv[1:])
    app = QApplication(sys.argv)
    ex = Example(address)
    ex.show()
    sys.exit(app.exec())