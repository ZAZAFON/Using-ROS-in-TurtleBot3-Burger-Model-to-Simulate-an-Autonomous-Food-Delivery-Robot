import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from robot_controller import RobotController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.robot_controller = RobotController()

        self.pushButton_seat1.clicked.connect(self.robot_controller.go_to_seat1)
        self.pushButton_seat2.clicked.connect(self.robot_controller.go_to_seat2)
        self.pushButton_seat3.clicked.connect(self.robot_controller.go_to_seat3)
        self.pushButton_seat4.clicked.connect(self.robot_controller.go_to_seat4)
        self.pushButton_return_origin.clicked.connect(self.robot_controller.return_to_origin)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


