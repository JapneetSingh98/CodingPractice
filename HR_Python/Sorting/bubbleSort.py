'''
#!/bin/python3

import math
import os
import random
import re
import sys
'''

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0
    
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                numSwaps = numSwaps + 1
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp

    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
    
'''
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
'''