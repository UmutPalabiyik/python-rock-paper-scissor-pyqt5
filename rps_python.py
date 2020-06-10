# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Umut Bey/Desktop/RockPaperScissors/rps.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 734)
        MainWindow.setMinimumSize(QtCore.QSize(1108, 734))
        MainWindow.setMaximumSize(QtCore.QSize(1108, 734))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/gameico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(24, 45))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"\n"
"    \n"
"    background-color: rgb(185, 123, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label_paper = QtWidgets.QLabel(self.centralwidget)
        self.label_paper.setGeometry(QtCore.QRect(860, 330, 81, 81))
        self.label_paper.setMaximumSize(QtCore.QSize(81, 16777215))
        self.label_paper.setStyleSheet("border-image: url(:/icons/justPaper.png);")
        self.label_paper.setText("")
        self.label_paper.setObjectName("label_paper")
        self.label_rock = QtWidgets.QLabel(self.centralwidget)
        self.label_rock.setGeometry(QtCore.QRect(850, 330, 91, 81))
        self.label_rock.setStyleSheet("border-image: url(:/icons/justRock.png);")
        self.label_rock.setText("")
        self.label_rock.setObjectName("label_rock")
        self.label_scissors = QtWidgets.QLabel(self.centralwidget)
        self.label_scissors.setGeometry(QtCore.QRect(850, 330, 91, 81))
        self.label_scissors.setStyleSheet("border-image: url(:/icons/justScissors.png);")
        self.label_scissors.setText("")
        self.label_scissors.setObjectName("label_scissors")
        self.pushButton_playButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_playButton.setGeometry(QtCore.QRect(500, 480, 131, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_playButton.setFont(font)
        self.pushButton_playButton.setStyleSheet("QPushButton{\n"
"    border-radius : 60px;\n"
"    background-color: rgb(255, 58, 24);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 0, 4);\n"
"    font: 75 20pt \"MS Shell Dlg 2\"\n"
"\n"
"}")
        self.pushButton_playButton.setObjectName("pushButton_playButton")
        self.pushButton_Paper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Paper.setGeometry(QtCore.QRect(270, 330, 91, 81))
        self.pushButton_Paper.setStyleSheet("QPushButton{\n"
"\n"
"    border-image: url(:/icons/justPaper.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(99, 189, 186);\n"
"}")
        self.pushButton_Paper.setText("")
        self.pushButton_Paper.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_Paper.setObjectName("pushButton_Paper")
        self.pushButton_Rock = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Rock.setGeometry(QtCore.QRect(60, 330, 91, 81))
        self.pushButton_Rock.setStyleSheet("QPushButton{\n"
"\n"
"    border-image: url(:/icons/justRock.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 101, 24);\n"
"    background-color: rgb(242, 102, 81);\n"
"}\n"
"")
        self.pushButton_Rock.setText("")
        self.pushButton_Rock.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_Rock.setObjectName("pushButton_Rock")
        self.pushButton_Scissors = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Scissors.setGeometry(QtCore.QRect(170, 230, 91, 81))
        self.pushButton_Scissors.setStyleSheet("QPushButton{\n"
"\n"
"    border-image: url(:/icons/justScissors.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(246, 189, 74);\n"
"}\n"
"")
        self.pushButton_Scissors.setText("")
        self.pushButton_Scissors.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_Scissors.setObjectName("pushButton_Scissors")
        self.label_playerScoreText = QtWidgets.QLabel(self.centralwidget)
        self.label_playerScoreText.setGeometry(QtCore.QRect(150, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_playerScoreText.setFont(font)
        self.label_playerScoreText.setStyleSheet("")
        self.label_playerScoreText.setObjectName("label_playerScoreText")
        self.label_computerScoreText = QtWidgets.QLabel(self.centralwidget)
        self.label_computerScoreText.setGeometry(QtCore.QRect(800, 440, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_computerScoreText.setFont(font)
        self.label_computerScoreText.setStyleSheet("")
        self.label_computerScoreText.setObjectName("label_computerScoreText")
        self.label_playerScore = QtWidgets.QLabel(self.centralwidget)
        self.label_playerScore.setGeometry(QtCore.QRect(190, 490, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_playerScore.setFont(font)
        self.label_playerScore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_playerScore.setObjectName("label_playerScore")
        self.label_computerScore = QtWidgets.QLabel(self.centralwidget)
        self.label_computerScore.setGeometry(QtCore.QRect(870, 500, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_computerScore.setFont(font)
        self.label_computerScore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_computerScore.setObjectName("label_computerScore")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 80, 701, 111))
        self.label.setStyleSheet("border-image: url(:/icons/titleOfGame - Kopya.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_playerWonText = QtWidgets.QLabel(self.centralwidget)
        self.label_playerWonText.setGeometry(QtCore.QRect(490, 220, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_playerWonText.setFont(font)
        self.label_playerWonText.setAlignment(QtCore.Qt.AlignCenter)
        self.label_playerWonText.setObjectName("label_playerWonText")
        self.label_computerWonText = QtWidgets.QLabel(self.centralwidget)
        self.label_computerWonText.setGeometry(QtCore.QRect(500, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_computerWonText.setFont(font)
        self.label_computerWonText.setObjectName("label_computerWonText")
        self.label_computerWonPic = QtWidgets.QLabel(self.centralwidget)
        self.label_computerWonPic.setGeometry(QtCore.QRect(490, 290, 161, 151))
        self.label_computerWonPic.setStyleSheet("border-image: url(:/icons/computerWinPic.png);")
        self.label_computerWonPic.setText("")
        self.label_computerWonPic.setObjectName("label_computerWonPic")
        self.label_playerWonPic = QtWidgets.QLabel(self.centralwidget)
        self.label_playerWonPic.setGeometry(QtCore.QRect(510, 300, 121, 111))
        self.label_playerWonPic.setStyleSheet("border-image: url(:/icons/playerWinPic.png);")
        self.label_playerWonPic.setText("")
        self.label_playerWonPic.setObjectName("label_playerWonPic")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.pushButton_playButton.setText(_translate("MainWindow", "PLAY"))
        self.label_playerScoreText.setText(_translate("MainWindow", "Player Score"))
        self.label_computerScoreText.setText(_translate("MainWindow", "Computer Score"))
        self.label_playerScore.setText(_translate("MainWindow", "0"))
        self.label_computerScore.setText(_translate("MainWindow", "0"))
        self.label_playerWonText.setText(_translate("MainWindow", "PLAYER WON"))
        self.label_computerWonText.setText(_translate("MainWindow", "COMPUTER WON"))

import icons_rc
