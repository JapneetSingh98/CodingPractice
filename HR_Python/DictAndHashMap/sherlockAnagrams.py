#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substrList = {}
    size = len(s) - 1
    while size > 0:
        for i in range(len(s) - size + 1):
            print(s[i:i+size])
            inOrder = ''.join(sorted(s[i:i+size]))
            
            if inOrder in substrList:
                substrList[inOrder] += 1
            else:
                substrList[inOrder] = 0
        size -= 1
        
    count = 0
    for key,value in substrList.items():
        count += (value*(value+1))/2
    return int(count)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

