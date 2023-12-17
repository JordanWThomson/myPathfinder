import pygame
import math
import os
from queue import PriorityQueue
import sys

import algorithms
import classes
import functions
import global_vars as gv
import presets

pygame.init()
#pygame.font.init()

pygame.display.set_icon(gv.myIcon)
pygame.display.set_caption("Pathfinder")

#MAIN
def main():

    mainGrid = functions.makeGrid()
    startCell = None #the cell where the path will begin.
    finalCell = None #the cell where the path will end.
    
    statesDict = {"menuState": True, "inProgressState": False, "completedState": 0, "selectedAlgorithm": False}
    
    textList = functions.renderText()
    textRectList = functions.positionText(textList)

    selectedPreset = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Left Click.
            if pygame.mouse.get_pressed()[0]:
                currentClickedCell = functions.getClickedCell(mainGrid)
                if currentClickedCell:
                    if (startCell == None) and currentClickedCell != finalCell:
                        startCell = currentClickedCell
                        startCell.makeStart()    
                    elif (finalCell == None) and currentClickedCell != startCell:
                        finalCell = currentClickedCell
                        finalCell.makeEnd()                        
                    elif currentClickedCell != startCell and currentClickedCell != finalCell:
                        currentClickedCell.makeBarrier()
            
            #Right Click.
            if pygame.mouse.get_pressed()[2]:
                currentClickedCell = functions.getClickedCell(mainGrid)
                if currentClickedCell:
                    if currentClickedCell == startCell:
                        startCell = None
                    elif currentClickedCell == finalCell:
                        finalCell = None
                    currentClickedCell.makeEmpty()
            
            #Keys.
            if event.type == pygame.KEYDOWN:
                #Any key escape from the program's completed state.
                if statesDict["completedState"] != 0:
                    statesDict["completedState"] = 0
                
                #Space Bar.
                if event.key == pygame.K_SPACE and (startCell and finalCell):
                    statesDict["inProgressState"] = True
                    for row in mainGrid:
                        for cell in row:
                            cell.updateNeighbourCells(mainGrid)
                    
                    if not statesDict["selectedAlgorithm"]:
                        pathScore, tickCounter = algorithms.aStarAlgorithm(mainGrid, startCell, finalCell,
                        lambda: functions.drawWindow(mainGrid, textList, textRectList, statesDict))
                    else:
                        pathScore, tickCounter = algorithms.DijkstraAlgorithm(mainGrid, startCell, finalCell,
                        lambda: functions.drawWindow(mainGrid, textList, textRectList, statesDict))
                    
                    if pathScore and tickCounter:
                        pathResultText = gv.myFont.render(str(pathScore), True, gv.textColor2)
                        textList[3][1] = pathResultText
                        timeResultText = gv.myFont.render(str(format(tickCounter/gv.fps, '.3f')) + 's', True, gv.textColor2)
                        textList[3][3] = timeResultText
                        statesDict["completedState"] = 1
                    else:
                        statesDict["completedState"] = 2
                    
                    statesDict["inProgressState"] = False
                
                #C Key.
                if event.key == pygame.K_c:
                    for row in mainGrid:
                        for cell in row:
                            cell.makeEmpty()
                            startCell = None
                            finalCell = None
                            
                #L Key.
                if event.key == pygame.K_l:
                    
                    for rowIndex, row in enumerate(presets.presetList[selectedPreset]):
                        for colIndex, value in enumerate(row):
                            if value == 0:
                                mainGrid[rowIndex][colIndex].makeEmpty()
                            elif value == 1:
                                mainGrid[rowIndex][colIndex].makeStart()
                                startCell = mainGrid[rowIndex][colIndex]
                            elif value == 2:
                                mainGrid[rowIndex][colIndex].makeEnd()
                                finalCell = mainGrid[rowIndex][colIndex]
                            elif value == 3:
                                mainGrid[rowIndex][colIndex].makeBarrier()
                                
                    selectedPreset +=1
                    if selectedPreset == len(presets.presetList):
                        selectedPreset = 0
                
                #S Key.
                if event.key == pygame.K_s and not statesDict["inProgressState"]:
                    statesDict["menuState"] = not statesDict["menuState"]
                
                #Q Key.
                if event.key == pygame.K_q:
                    statesDict["selectedAlgorithm"] = not statesDict["selectedAlgorithm"]
                
        functions.drawWindow(mainGrid, textList, textRectList, statesDict)
        
        gv.myClock.tick(gv.fps) #limit fps so program is easier to run. Also useful for testing/debugging.
        
main()