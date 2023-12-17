import pygame
import math
from sys import exit

import classes
import global_vars as gv

pygame.font.init()


def makeGrid():
    """
    Function that generates a grid of cell objects.
    """
    myGrid = []
    for row in range(gv.windowWidth//gv.cellWidth):
        myGrid.append([]) #add new empty list per row.
        for collumn in range(gv.windowWidth//gv.cellWidth):
            newCell = classes.Cell(row, collumn, gv.cellWidth)
            myGrid[row].append(newCell)
            
    return myGrid
    
    
def getClickedCell(grid):
    """
    Function that runs when the mouse is clicked. Gets the position of the click and returns
    the cell that was clicked, in any cell was.
    """
    mousePosition = pygame.mouse.get_pos()
    if (mousePosition[0] in range(gv.windowWidth)) and (mousePosition[1] in range(gv.windowWidth)):
        clickedRow = mousePosition[0] // gv.cellWidth
        clickedCol = mousePosition[1] // gv.cellWidth
        clickedCell = grid[clickedRow][clickedCol]
        
        return clickedCell
    
    else:
        return None
    
    
def getHScore(cellA, cellB):
    """
    Calculates and returns the rounded euclidian distance between 2 grid cells.
    """
    x1, y1 = cellA.rect.center
    x2, y2 = cellB.rect.center

    return round(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)))  
    
    
def renderText():
    """
    Function to render all text objects. Returns a list of all text objects.
    """
    #All the text to be displayed.
    #Main Panel Text.
    selectedAlgorithmText = gv.myFont.render("Algorithm:", True, gv.textColor1)
    algorithmText1 = gv.myFont.render("A*", True, gv.textColor2)
    algorithmText2 = gv.myFont.render("Dijkstra", True, gv.textColor2)
    swapMenuState_1Text = gv.myFontSmall.render("S Key = Controls", True, gv.textColor1)
    loadPresetText = gv.myFontSmall.render("L Key = Load Preset", True, gv.textColor1)
    
    #Results Panel Text
    pathText = gv.myFont.render("Path Cost:", True, gv.textColor1)
    pathResultText = gv.myFont.render("0", True, gv.textColor2)
    timeText = gv.myFont.render("Time:", True, gv.textColor1)
    timeResultText = gv.myFont.render("0", True, gv.textColor2)
    noPathText = gv.myFont.render("No Path Could Be Found.", True, gv.textColor1)
    
    #Controls Panel Text.
    leftClickText = gv.myFontSmall.render("L Click = Draw Cell", True, gv.textColor1)
    rightClickText = gv.myFontSmall.render("R Click = Erase Cell", True, gv.textColor1)
    spaceBarText = gv.myFontSmall.render("Space Bar = Start", True, gv.textColor1)
    cKeyText = gv.myFontSmall.render("C Key = Clear", True, gv.textColor1)
    qKeyText = gv.myFontSmall.render("Q Key = Swap Algorithm", True, gv.textColor1)  
    swapMenuState_2Text = gv.myFontSmall.render("S Key = Main Menu", True, gv.textColor1)
    
    #In Progress Panel Text.
    inProgressStateText = gv.myFont.render("Pathfinding In Progress...", True, gv.textColor1)
    
    textList = [[selectedAlgorithmText, algorithmText1, algorithmText2, swapMenuState_1Text, loadPresetText],
    [leftClickText, rightClickText, spaceBarText, cKeyText, qKeyText, swapMenuState_2Text],
    [inProgressStateText],
    [pathText, pathResultText, timeText, timeResultText, noPathText]]
    
    return textList


def positionText(textList):
    """
    Function to create and position rectangles from all text objects in textList.
    Returns a matching list of rectangles.
    """
    selectedAlgorithmTextRect = textList[0][0].get_rect(midleft=(20, gv.windowWidth+(gv.menuBarHeight//4)))
    algorithmText1Rect = textList[0][1].get_rect(midleft=(selectedAlgorithmTextRect.midright[0] + 5, gv.windowWidth+(gv.menuBarHeight//4)))
    algorithmText2Rect = textList[0][2].get_rect(midleft=(selectedAlgorithmTextRect.midright[0] + 5, gv.windowWidth+(gv.menuBarHeight//4)))
    swapMenuState_1TextRect = textList[0][3].get_rect(midleft=(20, gv.windowWidth + (3*gv.menuBarHeight//4)))
    loadPresetTextRect = textList[1][4].get_rect(midleft=(gv.windowWidth//2, gv.windowWidth+(3*gv.menuBarHeight//4)))
    
    leftClickTextRect = textList[1][0].get_rect(midleft=(20, gv.windowWidth+(gv.menuBarHeight//4)))
    rightClickTextRect = textList[1][1].get_rect(midleft=(leftClickTextRect.midleft[0], leftClickTextRect.midbottom[1] + 15))
    spaceBarTextRect = textList[1][2].get_rect(midleft=(gv.windowWidth//2, leftClickTextRect.midleft[1]))
    cKeyTextRect = textList[1][3].get_rect(midleft=(spaceBarTextRect.midleft[0], rightClickTextRect.midright[1]))
    qKeyTextRect = textList[1][4].get_rect(midleft=(spaceBarTextRect.midleft[0], gv.windowWidth+(3*gv.menuBarHeight//4)))
    swapMenuState_2TextRect = textList[1][5].get_rect(midleft=(20, gv.windowWidth+(3*gv.menuBarHeight//4)))
    
    inProgressStateTextRect = textList[2][0].get_rect(center=(gv.windowWidth//2, gv.windowWidth+(3*gv.menuBarHeight//4)))
    
    pathTextRect = textList[3][0].get_rect(midleft=(20, gv.windowWidth+(gv.menuBarHeight//4)))
    pathResultTextRect = textList[3][1].get_rect(midleft=(pathTextRect.midright[0] + 5, gv.windowWidth+(gv.menuBarHeight//4)))     
    timeTextRect = textList[3][2].get_rect(midleft=(gv.windowWidth//2, gv.windowWidth+(gv.menuBarHeight//4)))
    timeResultTextRect = textList[3][3].get_rect(midleft=(timeTextRect.midright[0] + 5, gv.windowWidth+(gv.menuBarHeight//4)))
    noPathTextRect = textList[3][4].get_rect(center=(gv.windowWidth//2, gv.windowWidth+(gv.menuBarHeight//4)))

    
    textRectList = [[selectedAlgorithmTextRect, algorithmText1Rect, algorithmText2Rect, swapMenuState_1TextRect, loadPresetTextRect],
    [leftClickTextRect, rightClickTextRect, spaceBarTextRect, cKeyTextRect, qKeyTextRect, swapMenuState_2TextRect],
    [inProgressStateTextRect],
    [pathTextRect, pathResultTextRect, timeTextRect, timeResultTextRect, noPathTextRect]]
    
    return textRectList


def drawWindow(grid, textList, textRectList, statesDict):
    """
    Function that handles all of the drawing to the window, using passed arguments to determine
    what is currently displayed on screen.
    """
    
    #Fill the background.
    gv.myWindow.fill('black')
    #Draws the cells that form the base grid.
    for row in grid:
        for cell in row:
            cell.drawCell()
    
    #Draw grid lines over the cells.
    for i in range(gv.windowWidth//gv.cellWidth):
        pygame.draw.line(gv.myWindow, 'black', (0, i*gv.cellWidth), (gv.windowWidth, i*gv.cellWidth))
        pygame.draw.line(gv.myWindow, 'black', (i*gv.cellWidth, 0), (i*gv.cellWidth, gv.windowWidth))

    #Draw text objects based on state.
    if statesDict["inProgressState"]:
        #Text that displays when the algorithm is running.
        gv.myWindow.blit(textList[3][0], textRectList[3][0])
        gv.myWindow.blit(textList[3][2], textRectList[3][2])
        gv.myWindow.blit(textList[2][0], textRectList[2][0])
    elif statesDict["completedState"] == 1:
        #Text that displays when the algorithm has finished.
        for i in range(len(textList[3])-1):
            gv.myWindow.blit(textList[3][i], textRectList[3][i])
    elif statesDict["completedState"] == 2:
        gv.myWindow.blit(textList[3][4], textRectList[3][4])
        
    else:
        #Text to display when the user has control/main menu.
        if statesDict["menuState"]: #show algorithms
            gv.myWindow.blit(textList[0][0], textRectList[0][0])
            if not statesDict["selectedAlgorithm"]:
                gv.myWindow.blit(textList[0][1], textRectList[0][1])
            else:
                gv.myWindow.blit(textList[0][2], textRectList[0][2])
            gv.myWindow.blit(textList[0][3], textRectList[0][3])
            gv.myWindow.blit(textList[0][4], textRectList[0][4])
        else: #show controls.
            for i in range(len(textList[1])):
                gv.myWindow.blit(textList[1][i], textRectList[1][i])

    pygame.display.update()
    
    
def drawPath(cellParentDict, start, currentChild, grid, drawWindow):
    """
    Function to visualise the final path between the start and end cells. Loops through all parent cells, starting
    with the end cell's parent and ending with the start cell, in the passed cellParentDict.
    Calculates and returns the total cost/distance of the path.
    """
    pathCost = 0
    currentChild.makeEnd()
    currentParent = cellParentDict[currentChild]
    while currentParent != start:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if (currentChild.row == currentParent.row) or (currentChild.col == currentParent.col): #if a diagonal movement...
            pathCost += 10
        else:
            pathCost += 14
        
        currentChild = currentParent
        currentChild.makePath()
        currentParent = cellParentDict[currentChild]
        
        drawWindow()
        
        gv.myClock.tick(gv.fps)
    
    #Add on path cost between start cell and its child.
    if (currentChild.row == currentParent.row) or (currentChild.col == currentParent.col):
        pathCost += 10
    else:
        pathCost += 14
        
    return pathCost