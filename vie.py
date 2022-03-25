import pygame, sys
from pygame.locals import *
import random

class Cell:

    def __init__(self):
        self.life = False
        self.neighbours = 0

    def setNeighbours(self, n):
        self.neighbours = n

    def getNeighbours(self):
        return self.neighbours

    def getLife(self):
        return self.life

    def setAlive(self):
        self.life = True

    def setDead(self):
        self.life = False


class Universe:

    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)
        self.universe = [[Cell() for i in range(self.height)] for j in range(self.width)]

    def getCell(self, x, y):
        return self.universe[x][y]

    def randomize(self):
        for x in range(self.width):
            for y in range(self.height):
#                print("Randomize : ", x,y)
                if random.randint(0, 1) == 1:
                    self.setAlive(x, y)

    #Draws the grid lines
    def drawGrid(self):
        """
        for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
        for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))
        """
        for x in range(self.width): # draw vertical lines
            for y in range (self.height): # draw horizontal lines
                if self.getCell(x, y).getLife():
                    pygame.draw.rect(DISPLAYSURF, GREEN, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))

    def countNeighbours(self, i , j):
        neighbours = 0
        for x in range (i-1,i+2):
            for y in range (j-1,j+2):
                if self.getLife(x, y) and (x!=i or y!=j):
                    neighbours += 1
        self.setNeighbours(i, j, neighbours)

    def tick(self):
        for x in range(self.width): 
            for y in range (self.height): 
                self.getCell(x, y).setNeighbours(self.countNeighbours(x, y))

        for x in range(self.width): 
            for y in range (self.height):
#                print("tick : ", x, y)
#                print(self.getNeighbours(x, y))

                n = self.getNeighbours(x, y)
                if n == None:
                    n = 0

                if n < 2 or n>3:
                    self.setDead(x, y)
                else:
                    self.setAlive(x, y)     

    def setNeighbours(self, x, y, n):
        print("setNeighbours : ", x, y, n)
        if x <= self.width and y <= self.height:
            self.getCell(x, y).setNeighbours(n)
        else:
            print("ERROR = out of scope parameters for setNeighbours")

    def getNeighbours(self, x, y):
#        print("getNeighbours : ", x, y)
        if x <= self.width and y <= self.height:
            print("getNeighbours : ", x, y, self.getCell(x, y).getNeighbours())
            return self.getCell(x, y).getNeighbours()
        else:
            print("ERROR = out of scope parameters for setNeighbours")
            return 0

    def setAlive(self, x, y):
#        print("setAlive : ", x, y)
        if x <= self.width and y <= self.height:
            self.getCell(x, y).setAlive()
            self.getCell(x, y).setNeighbours(0)
        else:
            print("ERROR = out of scope parameters for setAlive")

    def setDead(self, x, y):
#        print("setDead : ", x, y)
        if x <= self.width and y <= self.height:
            self.getCell(x, y).setDead()
            self.getCell(x, y).setNeighbours(0)
        else:
            print("ERROR = out of scope parameters for setDead")

    def getLife(self, x, y):
        if x<0 or x>=self.width or y<0 or y>=self.height:
            return False
        else:
            return self.getCell(x, y).getLife()

WINDOWWIDTH = 800
WINDOWHEIGHT = 400
CELLSIZE = 10

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE) # number of cells wide
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE) # Number of cells high

# set up the colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)
GREEN =    (0,  255,0)


def main():
    pygame.init()

    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    DISPLAYSURF.fill(WHITE) #fills the screen white

    pygame.display.set_caption('Game of Life')

    game = Universe(CELLHEIGHT, CELLWIDTH)
    game.randomize()
    game.setAlive(10, 10)
    game.setAlive(11, 10)
    game.setAlive(12, 10)
#    print (str(game))

    game.drawGrid()
    pygame.display.update()

         
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
#        game.tick()
#        game.drawGrid()
        pygame.display.update()

main()

if __name__=='__main__':
    main()

"""    
game = Universe(20)

game.setAlive(10, 10)
game.setAlive(11, 10)
game.setAlive(10, 11)

print (str(game))

"""
