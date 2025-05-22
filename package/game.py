import pygame
import random

class element():
    def __init__(self,x,y,size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color


class player(element):
    def __init__(self):
        super().__init__(0, 60, 20, (255,255,255))
        self.len = [{'x': self.x, 'y': self.y}]
        self.direction = 'right'

    def pos(self):
        return [self.x, self.y]


    def draw(self, window):
        for i in self.len:
            pygame.draw.rect(window,self.color, [i['x'],i['y'],self.size,self.size])

    def move(self):
        match self.direction:
            case 'right':
                self.x += round(self.size / 20) * 20
                if self.x >= 500:
                    self.x = 0
            case 'left':
                self.x -= round(self.size / 20) * 20
                if self.x < 0:
                    self.x = 500
                    self.x -= round(self.size / 20) * 20
            case 'up':
                self.y -= round(self.size / 20) * 20
                if self.y < 50:
                    self.y = round(540/20) * 20
            case 'down':
                self.y += round(self.size / 20) * 20
                if self.y >= 560:
                    self.y = round(60/20) * 20
        i = 0

        for i in range(len(self.len) - 1):

            self.len[i]['x'] = self.len[i + 1]['x']
            self.len[i]['y'] = self.len[i + 1]['y']
            i += 1

        self.len[-1] = {'x': self.x, 'y': self.y}
    
    def turnDirection(self,key):
        match key.upper():
            case 'D':
                if self.direction == "left":
                    return
                self.direction = 'right'
                return 
            case 'A':
                if self.direction == "right":
                    return
                self.direction = 'left'
                return 
            case 'W':
                if self.direction == "down":
                    return
                self.direction = 'up'
                return 
            case 'S':
                if self.direction == "up":
                    return
                self.direction = 'down'
                return
        
    def increaseLen(self):
        self.len.append({'x': self.x + 1, 'y': self.y})
         
    def checkPlayerColison(self):
        for i in range(len(self.len) - 1):
            if self.len[i]['x'] == self.x and self.len[i]['y'] == self.y:
                return True
        return False

class food(element):
    def __init__(self):
        super().__init__(20,20,20, (252,3,3))
        self.x = round(random.randrange(0,500 - self.size) / 20) * 20
        self.y = round(random.randrange(60,560 - self.size) / 20) * 20
    def drawFood(self,window):
         pygame.draw.rect(window,self.color, [self.x,self.y,self.size,self.size])

    def resetPos(self,player):
        self.x = round(random.randrange(0,500 - self.size) / 20) * 20
        self.y = round(random.randrange(60,560 - self.size) / 20) * 20
        playerPos = player.pos()
        if playerPos[0] == self.x and playerPos[1] == self.y:
           self.resetPos(player)