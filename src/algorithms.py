import pygame
from queue import PriorityQueue
from sys import exit

import functions
import global_vars as gv


def aStarAlgorithm(grid, start, final, drawWindow):
    openSet = PriorityQueue()
    openSet_follower = set() #a copy of priority queue, used to check the contents of the queue (since queues cannot be checked directly).
    closedSet = set() #a set within which we will store cells that have been calculated.
    cellParents = {} #a dictionary within which we will store each cell (as a key) and their associated parent cell.
    cellIndex = 0 #an incrementing counter to uniquely identify each cell; this value will act as a tiebreaker in the event that 2 or more cells have identical f-scores and h-scores and thus the same priority.
    tickCounter = 0 #a counter that will be used to store the number of ticks needed to complete the algorithm, then used along with fps to calculate time the algorithm took to complete.
    
    startGScore = 0 #distance travelled from beginning.
    startHScore = functions.getHScore(start, final) #estimated distance from end.
    startFScore = startGScore + startHScore #lower F scores are evaluated first, indicates most efficient path.
    
    openSet.put((startFScore, startHScore, cellIndex, startGScore, start)) #fscore listed 1st for better priority.
    openSet_follower.add(start)
    
    while not openSet.empty():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        currentData = openSet.get()
        currentFScore = currentData[0]
        currentHScore = currentData[1]
        #cellIndex is stored in currentData[2], we do not need it for any reason other than giving unique priority in the event that 2 or more cells in the queue have identical f and h scores.
        currentGScore = currentData[3]
        currentCell = currentData[4]
        
        if currentCell != start:
            currentCell.makeClosed()
        openSet_follower.remove(currentCell)
        closedSet.add(currentCell)
        
        if currentCell == final:
            pathScore = functions.drawPath(cellParents, start, final, grid, lambda: drawWindow())
            return pathScore, tickCounter
            
        for neighbourCell in currentCell.neighbourCells:
            if neighbourCell.isBarrier() or neighbourCell in closedSet:
                pass
            else:
                if (neighbourCell.row == currentCell.row) or (neighbourCell.col == currentCell.col): #if not diagonal...
                    plusGScore = 10
                else:
                    plusGScore = 14 #rounded value for diagonal distance between 2 adjacent cells.
                    
                neighbourGScore = currentGScore + plusGScore
                neighbourHScore = functions.getHScore(neighbourCell, final)
                neighbourFScore = neighbourGScore + neighbourHScore
                
                cellIndex += 1
                
                if (neighbourCell not in openSet_follower) or neighbourGScore < currentGScore:
                    cellParents[neighbourCell] = currentCell
                    neighbourCell.makeOpen()
                    openSet.put((neighbourFScore, neighbourHScore, cellIndex, neighbourGScore, neighbourCell))
                    openSet_follower.add(neighbourCell)
        
        drawWindow()
        gv.myClock.tick(gv.fps)
        tickCounter += 1
        
    return None, None
    
    
def DijkstraAlgorithm(grid, start, final, drawWindow):
    openSet = PriorityQueue()
    openSet_follower = set()
    closedSet = set()
    cellParents = {}
    cellIndex = 0
    tickCounter = 0
    #1. Initialise all cells (except start, which = 0) to have infinite as the time to travel from start (g score, in terms of a*).
    travelTime = {}
    for row in grid:
        for cell in row:
            travelTime[cell] = float("inf")
            cellParents[cell] = None
            
    travelTime[start] = 0
    openSet.put((travelTime[start], cellIndex, start))
    openSet_follower.add(start)
    #2. update estimated time to travel by adding the distance scores (10 or 14) to all neighbouring cells.
    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        currentData = openSet.get()
        currentTravelTime = currentData[0]
        #cell index in currentData[1] probably.
        currentCell = currentData[2]
        
        if currentCell != start:
            closedSet.add(currentCell)
            openSet_follower.remove(currentCell)
            currentCell.makeClosed()
        
        if currentCell == final:
            pathScore = functions.drawPath(cellParents, start, final, grid, lambda: drawWindow())
            return pathScore, tickCounter
            
        for neighbourCell in currentCell.neighbourCells:
            if neighbourCell.isBarrier() or (neighbourCell in closedSet) or neighbourCell in openSet_follower:
                pass
            else:
                if neighbourCell.row == currentCell.row or neighbourCell.col == currentCell.col:
                    plusTravelTime = 10
                else:
                    plusTravelTime = 14
                    
                neighbourTravelTime = travelTime[currentCell] + plusTravelTime
                    
                cellIndex += 1
                    
                if neighbourTravelTime < travelTime[neighbourCell]:
                    travelTime[neighbourCell] = neighbourTravelTime #update with new shorter travel time.
                    cellParents[neighbourCell] = currentCell
                    neighbourCell.makeOpen()
                    openSet.put((travelTime[neighbourCell], cellIndex, neighbourCell))
                    openSet_follower.add(neighbourCell)
               
        drawWindow()
        gv.myClock.tick(gv.fps)
        tickCounter += 1 
                    
    return None, None 