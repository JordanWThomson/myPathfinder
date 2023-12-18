import pygame

import global_vars as gv

class Cell:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.color = 'dimgrey' #default color representing empty.
        self.rect = pygame.Rect(row*width, col*width, width, width)
        self.neighbourCells = []
        
    def drawCell(self):
        pygame.draw.rect(gv.myWindow, self.color, self.rect)
        
    def makeStart(self):
        self.color = 'green'
        
    def isStart(self):
        return self.color == 'green'
        
    def makeEnd(self):
        self.color = 'red'
        
    def isEnd(self):
        return self.color == 'red'
        
    def makePath(self):
        self.color = 'white'
        
    def makeOpen(self):
        self.color = 'gold'
        
    def makeClosed(self):
        self.color = 'goldenrod'
        
    def makeBarrier(self):
        self.color = 'black'
        
    def isBarrier(self):
        return self.color == 'black'
        
    def makeEmpty(self):
        self.color = 'dimgrey'
        
    def updateNeighbourCells (self, grid):
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                elif self.row + i - 1 in range(gv.totalRows) and self.col + j - 1 in range(gv.totalRows):
                    validNeighbourCell = grid[self.row + i - 1][self.col + j -1]
                    self.neighbourCells.append(validNeighbourCell)
            
                """
                if i == 1 and j == 1:
                    continue
                elif (self.row > 0 and self.row < gv.windowWidth//gv.cellWidth - 1) and (self.col > 0 and self.col < gv.totalRows):  #Check if neighbour within grid bounds.
                    if not grid[self.row + i - 1][self.col + j - 1].isBarrier():
                        self.neighbourCells.append(grid[self.row + i - 1][self.col + j - 1])   ]
                """