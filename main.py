from pandas._libs.tslibs import Timestamp
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
        self.faz2_btn.clicked.connect(self.faz_two)

    def setDataDir(self):
        self.dataDir = str(QFileDialog.getExistingDirectory(
            None, "Select Directory"))

        if self.dataDir:
            self.label.setText("Data Path : " + self.dataDir)

            self.csvFile = [f for f in os.listdir(
                self.dataDir) if f.endswith(".csv")]

            self.comboBox.addItems(self.csvFile)

    def faz_one(self):

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

    def faz_two(self):
        faz_two_thread = threading.Thread(target=self.faz_two_thread)
        faz_two_thread.start()


    def faz_two_thread(self):
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        workerList = df.loc[(df["work"] == "سازمان بنادر") | (df["work"] == "گمرک")]["ssn"]
        workerList = list(item for item in workerList)
        df = pd.read_csv(os.path.join(self.dataDir, 'relationships.csv'))
        workersFamilyList = df.loc[df["from"].isin(workerList)]["to"]
        workersFamilyList = list(item for item in workersFamilyList)
        workersFamilyList.extend(workerList)
        ssnList = list(set(workersFamilyList))
        import datetime
        date = datetime.datetime.now().date() - datetime.timedelta(days=2*365)
        date = str(date)
        date = date.split('-')
        date = Timestamp(year=int(date[0]), month=int(date[1]), day=int(date[2]))
        df = pd.read_csv(os.path.join(self.dataDir, 'ownerships.csv'), parse_dates=[3])
        susList = df.loc[(df["from"].isin(ssnList)) & (df["date"] >= date)]["from"]
        susList = list(item for item in susList)
        susList = list(set(susList))
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        resultData = df.loc[df["ssn"].isin(susList)]
        temp = resultData.loc[(resultData["work"] != "سازمان بنادر") | (resultData["work"] != "گمرک")]["ssn"]
        temp = list(item for item in temp)
        df = pd.read_csv(os.path.join(self.dataDir, 'relationships.csv'))
        df = df.loc[(df["to"].isin(temp)) & df["from"].isin(workerList)]["from"]
        df = list(item for item in df)
        susList = set(susList) - set(temp)
        df.extend(susList)
        susList =list(set(df))
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        resultData = df.loc[df["ssn"].isin(susList)]
        resultData.to_csv(os.path.join(self.dataDir, 'faz2.csv'), columns=['first_name','last_name','ssn','birthday','city','work'], index=False)
        self.comboBox.addItem('faz2.csv')
        self.comboBox.setCurrentText('faz2.csv')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
