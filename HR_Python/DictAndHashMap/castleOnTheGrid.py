#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
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
    
    queue, visited = enqueue(queue, visited, startX, startY)
    while len(queue) > 0:
        queue, visited = search(queue, visited)
    

def enqueue(queue, visited, startX, startY):
    queue.append((startX,startY))
    visited[startX][startY] = "visited"
    return queue, visited

def search(queue, visited):
    curX, curY = queue[0]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

