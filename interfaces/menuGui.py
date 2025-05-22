from package.models.windowModel import Gui, label, btn
from interfaces.gameGui import initGame 

class menuGui(Gui):
    def __init__(self, us, leaderGui):
        super().__init__(440, 800, "Menu")

        self.styles = {
                'styleBtn': """
                QPushButton{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #00ff99, stop:1 #00ccff);
                    color: white;
                    border: none;
                    border-radius: 10px;
                    font-size: 30px;
                    color:white;
                }
                QPushButton:hover{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #00B36B, stop:1 #008FB3);
                }
            """,
        }

        self.user = us
        self.open = False
        self.leaderGUi = leaderGui
        label(f"Bem vindo {self.user['name']}", self.gui, 20, 50,"font-size: 30px; color: white;")
        gameBtn = btn("Jogar", self.gui, 110, 250, self.styles['styleBtn'], 220, 60)
        leaderBtn = btn("Raking", self.gui, 110, 400, self.styles['styleBtn'], 220, 60)

        gameBtn.pressBtn(self.gameInit)
        leaderBtn.pressBtn(self.leader)

    def gameInit(self):
        self.open = True
        self.exit()
        self.app.quit()
        initGame(self.user)

    def leader(self):
        self.gui.close()
        self.leaderGUi.show()
        self.leaderGUi.ranking()
        self.open = True
