from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_seat1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seat1.setGeometry(QtCore.QRect(50, 100, 150, 50))
        self.pushButton_seat1.setObjectName("pushButton_seat1")

        self.pushButton_seat2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seat2.setGeometry(QtCore.QRect(50, 160, 150, 50))
        self.pushButton_seat2.setObjectName("pushButton_seat2")

        self.pushButton_seat3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seat3.setGeometry(QtCore.QRect(200, 100, 150, 50))
        self.pushButton_seat3.setObjectName("pushButton_seat3")

        self.pushButton_seat4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seat4.setGeometry(QtCore.QRect(200, 160, 150, 50))
        self.pushButton_seat4.setObjectName("pushButton_seat4")

        self.pushButton_return_origin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_return_origin.setGeometry(QtCore.QRect(125, 220, 150, 50))
        self.pushButton_return_origin.setObjectName("pushButton_return_origin")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_seat1.setText(_translate("MainWindow", "Seat 1"))
        self.pushButton_seat2.setText(_translate("MainWindow", "Seat 2"))
        self.pushButton_seat3.setText(_translate("MainWindow", "Seat 3"))
        self.pushButton_seat4.setText(_translate("MainWindow", "Seat 4"))
        self.pushButton_return_origin.setText(_translate("MainWindow", "Return to Origin"))


