from ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.setDataPath_btn.clicked.connect(self.setDataDir)

    def setDataDir(self):
        self.dataDir = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.label.setText("Data Path : "+ self.dataDir)

    def faz_one(self):
        pass







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())