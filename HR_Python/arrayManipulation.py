'''
#!/bin/python3

import math
import os
import random
import re
import sys
'''

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    thisArray = [0] * n
    for step in queries:
        for i in range(step[0]-1, step[1]):
            thisArray[i] = thisArray[i] + step[2]
        
    return max(thisArray)


'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
'''