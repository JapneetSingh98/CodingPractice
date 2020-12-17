#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    groupList = []
    output = []
    #print(queries)
    for query in queries:
        inp = query
        
        firstLoc = None
        firstFound = False
        secondLoc = None
        secondFound = False
        for j in range(len(groupList)):
            if firstFound == False and inp[0] in groupList[j]:
                firstLoc = j
                firstFound = True
            if secondFound == False and inp[1] in groupList[j]:
                secondLoc = j
                secondFound = True
            if firstFound and secondFound:
                break
        if firstFound and secondFound:
            if firstLoc < secondLoc:
                for item in groupList[secondLoc]:
                    groupList[firstLoc].append(item)
                groupList.remove(groupList[secondLoc])
            elif secondLoc < firstLoc:
                for item in groupList[firstLoc]:
                    groupList[secondLoc].append(item)
                groupList.remove(groupList[firstLoc])
        elif firstFound:
            groupList[firstLoc].append(inp[1])
        elif secondFound:
            groupList[secondLoc].append(inp[0])
        else:
            groupList.append(inp)
            
        groupList.sort(key=len)
        groupList.reverse()
        print(groupList)
        output.append(len(groupList[0]))
        
    return output
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

