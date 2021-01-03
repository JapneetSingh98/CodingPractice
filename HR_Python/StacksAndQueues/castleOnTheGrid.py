#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    queue = []
    visited = []
    for i in range(len(grid)):
        col = []
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                col.append("open")
            else:
                col.append("blocked")
        visited.append(col)
    visited[goalX][goalY] = 'goal'
    
    queue, visited = enqueue(queue, visited, startX, startY, 0)

    while len(queue) > 0:
        queue, visited, reached = search(queue, visited)
    

def enqueue(queue, visited, curX, curY, num):
    queue.append((curX, curY))
    visited[curX][curY] = num
    return queue, visited

def search(queue, visited):
    curX, curY = queue[0]
    curN = visited[curX][curY]
    if curX == 0:                           # leftmost
        while curX < len(visited):
            if curX + 1 == len(visited):                # reached border
                break
            elif visited[curX + 1][curY] == 'blocked':  # reached block
                break
            else:                                       # space open, continue
                visited[curX+1][curY] = curN + 1
                curX += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        if visited[curX][curY] == 'goal':
                visited[curX][curY] = 

    elif curX == len(grid) - 1:             # rightmost

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
