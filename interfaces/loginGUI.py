from package.models.windowModel import Gui, label, inp, btn
from package.dataBaseControler import dataBase
from package.models.user import user

class loginGui(Gui):
    def __init__(self):
        super().__init__(440, 800, "login")
        self.styles = {
            'styleInput': """border-radius: 10px;
                color: "white";
                border:1px solid white;

            """,
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

            'createStyle': """
                QPushButton{
                    color: white;
                    font-size: 13px;
                    background: transparent;
                    border: none;
                }
                QPushButton:hover{

                }
        """}

        self.sucess = False
        
        label("Usuario", self.gui, 114, 275, "color:'white';")
        self.userInput = inp("", self.gui, 103, 300,self.styles['styleInput'],234, 41,)
        label("Senha", self.gui, 114, 359, "color:'white';")
        self.passwordInput = inp("", self.gui, 103, 384,self.styles['styleInput'] ,234, 41)
        loginBtn = btn("Login", self.gui, 124,500,self.styles['styleBtn'] ,192, 64)
        createBtn = btn("Novo Usuario", self.gui, 114, 420,self.styles['createStyle'] ,90, 70)
        self.mensage = label("", self.gui, 114, 70, "font-size: 20px; color: white;")

        loginBtn.pressBtn(self.login)
        createBtn.pressBtn(self.newUser)
    
    def newUser(self):
        us = user(self.userInput.inpt.text(), self.passwordInput.inpt.text())
        ver = dataBase.verindataB(us)
        if ver == False:
            if us.name != "" and us.password != "":
                dataBase.saveInDataBase(us.toDic())
                self.modifyMensage("Usuario Adicionado")
            else:
                self.modifyMensage("Usuario invalido")
        else:
            self.modifyMensage("Usuario ja existe")

    def login(self):
        us = dataBase.verindataB(user(self.userInput.inpt.text(), self.passwordInput.inpt.text()))
        if us != False:
            if us['password'] == self.passwordInput.inpt.text():
                self.sucess = True
                self.user = us
                self.exit()
            else:
                self.modifyMensage("Usuario/Senha invalidos")    
        
        else:
            self.modifyMensage("Usuario/Senha invalidos")

    
    def modifyMensage(self, txt):
        self.mensage.modifyTxt(txt, 220, 100)

