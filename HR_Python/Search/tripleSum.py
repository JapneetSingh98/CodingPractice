#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    
    arrs = [a, b, c]
    arrs[0].sort()
    arrs[1].sort()
    arrs[2].sort()
    
    for arr in arrs:                    # removes duplicates within each array
        prev = 0
        for i in arr:
            if i == prev:
                arr.remove(i)
            else:
                prev = i

    aCur = bCur = cCur = 0
    count = 0
    
    while bCur < len(arrs[1]):
        while aCur < len(arrs[0]) and arrs[0][aCur] <= arrs[1][bCur]:
            aCur = aCur + 1
        
        while cCur < len(arrs[2]) and arrs[2][cCur] <= arrs[1][bCur]:
            cCur = cCur + 1
        
        count = count + (aCur * cCur)
        bCur = bCur + 1
    
    return count

                
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

