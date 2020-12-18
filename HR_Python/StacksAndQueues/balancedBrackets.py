#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    openBrackets = ['{','(','[']
    opposites = {'}':'{', ')':'(', ']':'['}
    for char in s:
        if char in openBrackets:
            stack.append(char)
        elif len(stack) <= 0:
            return "NO"
        elif stack[len(stack)-1] == opposites[char]:
            stack.pop(len(stack)-1)
        else:
            return "NO"
    if len(stack) != 0:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

