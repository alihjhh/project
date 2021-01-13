from ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QHeaderView, QTableWidgetItem
import pandas as pd
import os
import threading
import time


class Ui(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.tableFlag = False
        self.faz1_btn.clicked.connect(self.setDataDir)
        self.comboBox.currentIndexChanged.connect(self.faz_one)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setDataDir(self):
        self.dataDir = str(QFileDialog.getExistingDirectory(
            None, "Select Directory"))

        if self.dataDir:
            self.label.setText("Data Path : " + self.dataDir)

            self.csvFile = [f for f in os.listdir(
                self.dataDir) if f.endswith(".csv")]

            self.comboBox.addItems(self.csvFile)

    def faz_one(self):
        show_data_thread = threading.Thread(target=self.show_data)
        show_data_thread.start()

    def show_data(self):

        if self.tableFlag:
            self.tableWidget.clearContents()
            self.tableWidget.clear()

        self.tableFlag = True
        df = pd.read_csv(os.path.join(
            self.dataDir, self.comboBox.currentText()))
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for x in range(df.shape[0]):
            for y, data in enumerate(df.loc[x]):
                self.tableWidget.setItem(x, y, QTableWidgetItem(str(data)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
