#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 1
    while i <= len(arr):
        #print(i)
        if arr[i-1] != i:
            temp = arr[i-1]
            arr[i-1] = arr[temp-1]
            arr[temp-1] = temp
            count += 1
            i -= 1
        i += 1
        #print(arr)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
