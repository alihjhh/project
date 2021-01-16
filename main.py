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
        self.faz3_btn.clicked.connect(self.faz_three)
        self.faz4_btn.clicked.connect(self.faz_four)

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

    def faz_three(self):
        result = []
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        df = df.loc[df["work"] == "قاچاقچی"]["ssn"]
        temp = list(item for item in df)
        del df
        dfacc = pd.read_csv(os.path.join(self.dataDir, 'accounts.csv'))
        ghachaghchiAcc = dfacc.loc[dfacc["ssn"].isin(temp)]["account_id"]
        del temp
        ghachaghchiAcc = list(item for item in ghachaghchiAcc)
        df = pd.read_csv(os.path.join(self.dataDir, 'faz2.csv'))["ssn"]
        temp = list(item for item in df)
        del df
        susAcc = dfacc.loc[dfacc["ssn"].isin(temp)]["account_id"]
        del temp
        del dfacc
        susAcc = list(item for item in susAcc)
        dfTemp = pd.read_csv(os.path.join(self.dataDir, 'transactions.csv'))
        df = dfTemp.loc[dfTemp["to"].isin(susAcc)]
        del dfTemp
        lvl1 = df.loc[df["from"].isin(ghachaghchiAcc)]["to"]
        lvl1 = list(item for item in lvl1)
        lvl1 = list(set(lvl1))
        result.extend(lvl1)
        df = df.loc[df["to"].isin(lvl1) == False]
        dfTransactoin = pd.read_csv(os.path.join(self.dataDir, 'transactions.csv'))
        df = df.reset_index(drop=True)

        for i in range(df.shape[0]):
            temp = df.loc[i][1]
            temp2 = [df.loc[i][0]]
            for i in range(5):
                dfTemp = dfTransactoin.loc[dfTransactoin["to"].isin(temp2)]
                dfTemp2 = dfTemp.loc[dfTemp["from"].isin(ghachaghchiAcc)]
                if(dfTemp2.shape[0] > 0):
                    result.append(temp)
                    break
                else:
                    temp2 = dfTransactoin.loc[dfTransactoin["to"].isin(temp2)]["from"]
                    temp2 = list(item for item in temp2)
        result = list(set(result))
        df = pd.read_csv(os.path.join(self.dataDir, 'accounts.csv'))
        temp = df.loc[df["account_id"].isin(result)]["ssn"]
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        df = df.loc[df["ssn"].isin(temp)]
        df.to_csv(os.path.join(self.dataDir, 'faz3.csv'), columns=['first_name','last_name','ssn','birthday','city','work'], index=False)
        self.comboBox.addItem('faz3.csv')
        self.comboBox.setCurrentText('faz3.csv')

    def faz_four(self):
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        df = df.loc[df["work"] == "قاچاقچی"]["ssn"]
        temp = list(item for item in df)
        df = pd.read_csv(os.path.join(self.dataDir, 'phones.csv'))
        df = df.loc[df["ssn"].isin(temp)]["number"]
        ghachaghchiPhone = list(item for item in df)
        df = pd.read_csv(os.path.join(self.dataDir, 'faz3.csv'))["ssn"]
        temp = list(item for item in df)
        df = pd.read_csv(os.path.join(self.dataDir, 'phones.csv'))
        df = df.loc[df["ssn"].isin(temp)]["number"]
        susPhone = list(item for item in df)
        df = pd.read_csv(os.path.join(self.dataDir, 'calls.csv'))
        dfTemp1 = df.loc[(df["from"].isin(ghachaghchiPhone)) & (df["to"].isin(susPhone))]["to"]
        dfTemp2 = df.loc[(df["from"].isin(susPhone)) & (df["to"].isin(ghachaghchiPhone))]["from"]
        df1 = list(item for item in dfTemp1)
        df2 = list(item for item in dfTemp2)
        df1 = list(set(df1))
        df2 = list(set(df2))
        df1.extend(df2)
        result = []
        for item in df1:
            if item in susPhone:
                result.append(item)
        df = pd.read_csv(os.path.join(self.dataDir, 'phones.csv'))
        df = df.loc[df["number"].isin(result)]["ssn"]
        df = list(item for item in df)
        resSSN = list(set(df))
        df = pd.read_csv(os.path.join(self.dataDir, 'people.csv'))
        df = df.loc[df["ssn"].isin(resSSN)]
        df.to_csv(os.path.join(self.dataDir, 'faz4.csv'), columns=['first_name','last_name','ssn','birthday','city','work'], index=False)
        self.comboBox.addItem('faz4.csv')
        self.comboBox.setCurrentText('faz4.csv')





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
