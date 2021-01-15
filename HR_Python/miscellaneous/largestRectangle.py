#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.

global curStreak
curStreak = []

def largestRectangle(h):
    largest = 0
    
    for i in range(len(h)):
        size = 1
        prev = i - 1
        while prev >= 0 and h[prev] >= h[i]:
            size += 1
            prev -= 1
        right = i + 1
        while right < len(h) and h[right] >= h[i]:
            size += 1
            right += 1
        if size*h[i] > largest:
            largest = size*h[i]

    return largest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()