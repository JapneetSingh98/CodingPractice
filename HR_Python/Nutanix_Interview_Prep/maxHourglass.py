#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    def calcHourglass(r, c):
        tot = sum(arr[r][c:c + 3])
        tot += arr[r + 1][c + 1]
        tot += sum(arr[r + 2][c:c + 3])
        return tot

    maxHG = calcHourglass(0, 0)
    for r in range(len(arr) - 2):
        for c in range(len(arr[0]) - 2):
            curHG = calcHourglass(r, c)
            if curHG > maxHG:
                maxHG = curHG

    return maxHG


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
