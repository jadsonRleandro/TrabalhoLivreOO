from interfaces.loginGUI import loginGui
from package.dataBaseControler import dataBase
from interfaces.menuGui import menuGui
from interfaces.leaderGui import leaderGui

def main():
    dataBase.load()
    login = loginGui()
    login.exe()

    if login.sucess == True:
        leader = leaderGui(login.user)
        menu = menuGui(login.user, leader)
        menu.exe()
        while menu.open == True:
            menu.open = False
            menu.exe()


if __name__ == "__main__":
    main()