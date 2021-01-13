# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 667)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setDataPath_btn = QtWidgets.QPushButton(self.centralwidget)
        self.setDataPath_btn.setObjectName("setDataPath_btn")
        self.horizontalLayout.addWidget(self.setDataPath_btn)
        self.faz1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.faz1_btn.setObjectName("faz1_btn")
        self.horizontalLayout.addWidget(self.faz1_btn)
        self.faz2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.faz2_btn.setObjectName("faz2_btn")
        self.horizontalLayout.addWidget(self.faz2_btn)
        self.faz3_btn = QtWidgets.QPushButton(self.centralwidget)
        self.faz3_btn.setObjectName("faz3_btn")
        self.horizontalLayout.addWidget(self.faz3_btn)
        self.faz4_btn = QtWidgets.QPushButton(self.centralwidget)
        self.faz4_btn.setObjectName("faz4_btn")
        self.horizontalLayout.addWidget(self.faz4_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setDataPath_btn.setText(_translate("MainWindow", "Set All Data Path"))
        self.faz1_btn.setText(_translate("MainWindow", "Faz 1"))
        self.faz2_btn.setText(_translate("MainWindow", "Faz 2"))
        self.faz3_btn.setText(_translate("MainWindow", "Faz 3"))
        self.faz4_btn.setText(_translate("MainWindow", "Faz 4"))
        self.label.setText(_translate("MainWindow", "Data Path : UNKNOWN"))
        self.label_2.setText(_translate("MainWindow", "Data : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
