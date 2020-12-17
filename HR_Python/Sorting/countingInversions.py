#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    count = 0
    return countHelp(arr, count)
def countHelp(arr, count):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            print(arr)
            arr[i-1],arr[i] = arr[i],arr[i-1]
            count = count + 1
    sortedarr = arr[:]
    sortedarr.sort()
    if sortedarr != arr:
        return countHelp(arr, count)
    else:
        print(arr)
        return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
