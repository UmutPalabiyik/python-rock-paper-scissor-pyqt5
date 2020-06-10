from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from rps_python import Ui_MainWindow
import random






class GameRPS(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #At first we hid text of who wonText and wonPic
        self.ui.label_playerWonText.setHidden(True)
        self.ui.label_playerWonPic.setHidden(True)
        self.ui.label_computerWonText.setHidden(True)
        self.ui.label_computerWonPic.setHidden(True)

        # At first we hid score table
        self.ui.label_playerScore.setHidden(True)
        self.ui.label_playerScoreText.setHidden(True)
        self.ui.label_computerScore.setHidden(True)
        self.ui.label_computerScoreText.setHidden(True)


        # At first we hid pushButtons of tools of game
        self.ui.pushButton_Paper.setVisible(False)
        self.ui.pushButton_Rock.setVisible(False)
        self.ui.pushButton_Scissors.setVisible(False)


        # At first we hid labels of tools of game
        self.ui.label_paper.setHidden(True)
        self.ui.label_rock.setHidden(True)
        self.ui.label_scissors.setHidden(True)




        # ==================  we connect buttons to functions ================================

        self.ui.pushButton_playButton.clicked.connect(self.startGame)
                
        # if i select paper
        self.ui.pushButton_Paper.clicked.connect(self.ifPaper)

        # if i select rock
        self.ui.pushButton_Rock.clicked.connect(self.ifRock)

        # if i select scissors
        self.ui.pushButton_Scissors.clicked.connect(self.ifScissors)

        # ===================================================================================




    def startGame(self):
        self.playerScoreO = 0
        self.computerScoreO = 0

        # we hid pics of win pose's and text of label until the game is over
        self.ui.label_playerWonPic.setHidden(True)
        self.ui.label_computerWonPic.setHidden(True)
        self.ui.label_computerWonText.setHidden(True)
        self.ui.label_playerWonText.setHidden(True)

        # Enabled push buttons cuz of the game started again
        self.ui.pushButton_Paper.setEnabled(True)
        self.ui.pushButton_Rock.setEnabled(True)
        self.ui.pushButton_Scissors.setEnabled(True)


        # We hid play button because the game started
        self.ui.pushButton_playButton.setVisible(False) 


        # we show score's labels again because
        self.ui.label_playerScore.setHidden(False)
        self.ui.label_playerScoreText.setHidden(False)
        self.ui.label_computerScore.setHidden(False)
        self.ui.label_computerScoreText.setHidden(False)

        

        self.ui.pushButton_Paper.setVisible(True)
        self.ui.pushButton_Rock.setVisible(True)
        self.ui.pushButton_Scissors.setVisible(True)

   
    def ifScissors(self):
        self.ui.label_paper.setHidden(True)
        self.ui.label_rock.setHidden(True)
        self.ui.label_scissors.setHidden(True) 

        i = random.choice([self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors,
                           self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors,
                           self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors])

        
        if i == self.ui.label_scissors:
            self.ui.label_scissors.setHidden(False)

        elif i == self.ui.label_rock:
            self.ui.label_rock.setHidden(False)
            self.computerScoreO += 1
            self.ui.label_computerScore.setText(str(self.computerScoreO))

        elif i == self.ui.label_paper:
            self.ui.label_paper.setHidden(False)
            self.playerScoreO += 1
            self.ui.label_playerScore.setText(str(self.playerScoreO))
        
        # we check who reached the first three points 
        if self.playerScoreO == 3:
            self.ui.label_playerWonText.setHidden(False)
            self.ui.label_playerWonPic.setHidden(False)


            # we reset score,victory pose and change play button to play again button
            self.ui.pushButton_playButton.setVisible(True) #we hid play button because the game started
            self.playerScoreO = 0
            self.computerScoreO = 0
            self.ui.label_playerScore.setText(str(self.playerScoreO))
            self.ui.label_computerScore.setText(str(self.computerScoreO))

            # deactivate the current button because of the round is over
            self.ui.pushButton_Paper.setEnabled(False)
            self.ui.pushButton_Rock.setEnabled(False)
            self.ui.pushButton_Scissors.setEnabled(False)


        if self.computerScoreO == 3:
            self.ui.label_computerWonText.setHidden(False)
            self.ui.label_computerWonPic.setHidden(False)

            # we reset score,victory pose and change play button to play again button
            self.ui.pushButton_playButton.setVisible(True) #we hid play button because the game started
            self.playerScoreO = 0
            self.computerScoreO = 0
            self.ui.label_playerScore.setText(str(self.playerScoreO))
            self.ui.label_computerScore.setText(str(self.computerScoreO))


            # deactivate the current button because of the round is over
            self.ui.pushButton_Paper.setEnabled(False)
            self.ui.pushButton_Rock.setEnabled(False)
            self.ui.pushButton_Scissors.setEnabled(False)
        #=============================================

        

    
    def ifRock(self):
        self.ui.label_paper.setHidden(True)
        self.ui.label_rock.setHidden(True)
        self.ui.label_scissors.setHidden(True)   

        i = random.choice([self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors,
                           self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors,
                           self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors])

        if i == self.ui.label_rock:
            self.ui.label_rock.setHidden(False)


        elif  i == self.ui.label_scissors:
            self.ui.label_scissors.setHidden(False)         
            self.playerScoreO += 1
            self.ui.label_playerScore.setText(str(self.playerScoreO))

        elif i == self.ui.label_paper:
            self.ui.label_paper.setHidden(False)
            self.computerScoreO += 1
            self.ui.label_computerScore.setText(str(self.computerScoreO))

        
        # we check who reached the first three points 
        if self.playerScoreO == 3:
            self.ui.label_playerWonText.setHidden(False)
            self.ui.label_playerWonPic.setHidden(False)

            # we reset score,victory pose and change play button to play again button
            self.ui.pushButton_playButton.setVisible(True) #we hid play button because the game started
            self.playerScoreO = 0
            self.computerScoreO = 0
            self.ui.label_playerScore.setText(str(self.playerScoreO))
            self.ui.label_computerScore.setText(str(self.computerScoreO))

            # deactivate the current button because of the round is over
            self.ui.pushButton_Paper.setEnabled(False)
            self.ui.pushButton_Rock.setEnabled(False)
            self.ui.pushButton_Scissors.setEnabled(False)

        if self.computerScoreO == 3:
            self.ui.label_computerWonText.setHidden(False)
            self.ui.label_computerWonPic.setHidden(False)


            # we reset score,victory pose and change play button to play again button
            self.ui.pushButton_playButton.setVisible(True) #we hid play button because the game started
            self.playerScoreO = 0
            self.computerScoreO = 0
            self.ui.label_playerScore.setText(str(self.playerScoreO))
            self.ui.label_computerScore.setText(str(self.computerScoreO))

            # deactivate the current button because of the round is over
            self.ui.pushButton_Paper.setEnabled(False)
            self.ui.pushButton_Rock.setEnabled(False)
            self.ui.pushButton_Scissors.setEnabled(False)


        #=============================================
      
    def ifPaper(self): 
        self.ui.label_paper.setHidden(True)
        self.ui.label_rock.setHidden(True)
        self.ui.label_scissors.setHidden(True)

        i = random.choice([self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors,
                           self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors,
                           self.ui.label_paper,self.ui.label_rock,self.ui.label_scissors])

        if i == self.ui.label_rock:
            self.ui.label_rock.setHidden(False)
            self.playerScoreO += 1
            self.ui.label_playerScore.setText(str(self.playerScoreO))

        elif  i == self.ui.label_scissors:
            self.ui.label_scissors.setHidden(False)         
            self.computerScoreO += 1
            self.ui.label_computerScore.setText(str(self.computerScoreO))



        elif i == self.ui.label_paper:
            self.ui.label_paper.setHidden(False)


        # we check who reached the first three points 
        if self.playerScoreO == 3:
            self.ui.label_playerWonText.setHidden(False)
            self.ui.label_playerWonPic.setHidden(False)

            # we reset score,victory pose and change play button to play again button
            self.ui.pushButton_playButton.setVisible(True) #we hid play button because the game started
            self.playerScoreO = 0
            self.computerScoreO = 0
            self.ui.label_playerScore.setText(str(self.playerScoreO))
            self.ui.label_computerScore.setText(str(self.computerScoreO))

            # deactivate the current button because of the round is over
            self.ui.pushButton_Paper.setEnabled(False)
            self.ui.pushButton_Rock.setEnabled(False)
            self.ui.pushButton_Scissors.setEnabled(False)

        if self.computerScoreO == 3:
            self.ui.label_computerWonText.setHidden(False)
            self.ui.label_computerWonPic.setHidden(False)

            # we reset score,victory pose and change play button to play again button
            self.ui.pushButton_playButton.setVisible(True) #we hid play button because the game started
            self.playerScoreO = 0
            self.computerScoreO = 0
            self.ui.label_playerScore.setText(str(self.playerScoreO))
            self.ui.label_computerScore.setText(str(self.computerScoreO))

            # deactivate the current button because of the round is over
            self.ui.pushButton_Paper.setEnabled(False)
            self.ui.pushButton_Rock.setEnabled(False)
            self.ui.pushButton_Scissors.setEnabled(False)
        #=============================================


        



app = QApplication([])
win = GameRPS()
win.show()
app.exec_()