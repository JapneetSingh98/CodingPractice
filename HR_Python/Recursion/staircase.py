#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    reference = [None]*(n+1)
    #print(len(reference))
    return stepPermsHelper(reference, n)
def stepPermsHelper(reference, n):
    #print(n)
    #print(reference)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif reference[n] != None:
        return reference[n]
    else:
        reference[n] = stepPermsHelper(reference, n-1) + stepPermsHelper(reference, n-2) + stepPermsHelper(reference, n-3)
        return reference[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

