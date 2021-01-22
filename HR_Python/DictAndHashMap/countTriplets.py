#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    secondNum = []
    thirdNum = []
    for item in arr:
        for third in thirdNum:
            if third == item:
                count += 1
        for second in secondNum:
            if second == item:
                thirdNum.append(item*r)
        secondNum.append(item*r)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
