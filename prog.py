import sys
from main import get_picture
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from design import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self, pict):
        super().__init__()
        self.setupUi(self)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(pict)
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    address = " ".join(sys.argv[1:])
    pict = get_picture(address, with_label=True)
    app = QApplication(sys.argv)
    ex = Example(pict)
    ex.show()
    sys.exit(app.exec())