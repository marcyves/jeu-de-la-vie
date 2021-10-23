import pygame, sys
from pygame.locals import *
import random

class Cell:

    def __init__(self):
        self.life = False

    def isAlive(self):
        return self.life

    def setAlive(self):
        self.life = True

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
        for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
        for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))
            
        for x in range(self.width): # draw vertical lines
            for y in range (self.height): # draw horizontal lines
                if self.getCell(x, y).isAlive():
                    pygame.draw.rect(DISPLAYSURF, GREEN, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))

    def __str__(self):
        for line in self.universe:
            for cell in line:
                if cell.isAlive():
                    print("X", end= '' )
                else:
                    print("_", end= '' )
            print(' ')

    def setAlive(self, x, y):
#        print("setAlive : ", x, y)
        if x <= self.width and y <= self.height:
            self.universe[x][y].setAlive()
        else:
            print("ERROR = out of scope parameters for setAlive")

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
#    game.randomize()
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
