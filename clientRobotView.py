# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientRobotView.ui'
#
# Created: Sun Apr 17 14:27:50 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Robot(object):
    def setupUi(self, Robot):
        Robot.setObjectName(_fromUtf8("Robot"))
        Robot.resize(700, 230)
        self.centralwidget = QtGui.QWidget(Robot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 191, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButtonConnect = QtGui.QPushButton(self.groupBox)
        self.pushButtonConnect.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButtonConnect.setObjectName(_fromUtf8("pushButtonConnect"))
        self.pushButtonDeconnect = QtGui.QPushButton(self.groupBox)
        self.pushButtonDeconnect.setGeometry(QtCore.QRect(100, 110, 75, 23))
        self.pushButtonDeconnect.setObjectName(_fromUtf8("pushButtonDeconnect"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditPort = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.gridLayout.addWidget(self.lineEditPort, 1, 1, 1, 1)
        self.lineEditIP = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditIP.setObjectName(_fromUtf8("lineEditIP"))
        self.gridLayout.addWidget(self.lineEditIP, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 40, 421, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEditFromServer = QtGui.QTextEdit(self.groupBox_2)
        self.textEditFromServer.setGeometry(QtCore.QRect(10, 20, 401, 111))
        self.textEditFromServer.setObjectName(_fromUtf8("textEditFromServer"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        Robot.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Robot)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Robot.setStatusBar(self.statusbar)

        self.retranslateUi(Robot)
        QtCore.QMetaObject.connectSlotsByName(Robot)

    def retranslateUi(self, Robot):
        Robot.setWindowTitle(_translate("Robot", "MainWindow", None))
        self.groupBox.setTitle(_translate("Robot", "Connection", None))
        self.pushButtonConnect.setText(_translate("Robot", "Connect", None))
        self.pushButtonDeconnect.setText(_translate("Robot", "Deconnect", None))
        self.lineEditPort.setText(_translate("Robot", "6008", None))
        self.lineEditIP.setText(_translate("Robot", "192.168.1.55", None))
        self.label.setText(_translate("Robot", "IP :", None))
        self.label_2.setText(_translate("Robot", "Port :", None))
        self.groupBox_2.setTitle(_translate("Robot", "From server", None))
        self.label_3.setText(_translate("Robot", "ROBOT", None))

