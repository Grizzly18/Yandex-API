# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 701, 581))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.PgUp = QtWidgets.QPushButton(self.centralwidget)
        self.PgUp.setGeometry(QtCore.QRect(720, 10, 61, 61))
        self.PgUp.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/PgUp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PgUp.setIcon(icon)
        self.PgUp.setIconSize(QtCore.QSize(50, 100))
        self.PgUp.setObjectName("PgUp")
        self.PgDown = QtWidgets.QPushButton(self.centralwidget)
        self.PgDown.setGeometry(QtCore.QRect(790, 10, 61, 61))
        self.PgDown.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/PgDown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PgDown.setIcon(icon1)
        self.PgDown.setIconSize(QtCore.QSize(50, 100))
        self.PgDown.setObjectName("PgDown")
        self.Right = QtWidgets.QPushButton(self.centralwidget)
        self.Right.setGeometry(QtCore.QRect(800, 110, 31, 28))
        self.Right.setObjectName("Right")
        self.Left = QtWidgets.QPushButton(self.centralwidget)
        self.Left.setGeometry(QtCore.QRect(740, 110, 31, 28))
        self.Left.setObjectName("Left")
        self.Down = QtWidgets.QPushButton(self.centralwidget)
        self.Down.setGeometry(QtCore.QRect(770, 110, 31, 28))
        self.Down.setObjectName("Down")
        self.Up = QtWidgets.QPushButton(self.centralwidget)
        self.Up.setGeometry(QtCore.QRect(770, 80, 31, 28))
        self.Up.setObjectName("Up")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Right.setText(_translate("MainWindow", "🡲"))
        self.Left.setText(_translate("MainWindow", "🡰"))
        self.Down.setText(_translate("MainWindow", "🡳"))
        self.Up.setText(_translate("MainWindow", "🡱"))
