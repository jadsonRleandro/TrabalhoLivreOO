import pygame
from package.models.windowModel import window
from package.game import player, food
from package.dataBaseControler import dataBase

colors = {
    'black': (0,0,0),
    'red': (252,3,3),
    'white': (255,255,255),
    'green': (15, 153, 0)
}

class initGame(window):
    def __init__(self, us):
        super().__init__(500, 560, "Jogo")
        self.points = 0
        self.record = us['record']
        self.user = us

        pygame.init()
        self.win = pygame.display.set_mode((self.height, self.width))
        self.player = player()
        self.food = food()
        self.gameOver = False
        self.spd = 15

        self.loop()

    def loop(self):
        while not self.gameOver:
            
            self.win.fill(colors['green'])
            self.player.draw(self.win)
            self.player.move()
            self.food.drawFood(self.win)
            self.drawPoints()
            self.checkcolision()
            self.checkRecord()
            for envent in pygame.event.get():

                if envent.type == pygame.QUIT:
                    self.quit()
                
                elif envent.type == pygame.KEYDOWN:
                    self.player.turnDirection(envent.unicode)

            pygame.display.update()
            pygame.time.Clock().tick(self.spd)
        pygame.quit()

    def drawPoints(self):
        pygame.draw.rect(self.win, colors['black'], [0,0, 500, 60])

        font = pygame.font.SysFont("Arial", 30)
        point = font.render(f"Pontos: {self.points}", True, colors['white'])
        self.win.blit(point, [10,10])
        record = font.render(f"Record: {self.record}", True, colors['white'])
        self.win.blit(record, [320, 10])
    
    def checkcolision(self):
        if self.player.checkPlayerColison() == True:
            self.quit()

        if self.player.x == self.food.x and self.player.y == self.food.y:
            self.player.increaseLen()
            self.food.resetPos(self.player) 
            self.points += 2

    def checkRecord(self):
        if self.points > self.record:
            self.record = self.points
        
    def quit(self):
        self.gameOver = True
        self.user['record'] = self.record
        dataBase.saveInDataBase(self.user)

        