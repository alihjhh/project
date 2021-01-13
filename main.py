from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui(Ui_MainWindow):

    def test(self):
        pass








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())