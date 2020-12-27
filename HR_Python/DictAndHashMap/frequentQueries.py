#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    arr = []
    freq = {}
    
    for q in queries:
        if q[0] == 1:
            arr.append(q[1])
            if q[1] in freq:
                freq[q[1]] += 1
            else:
                freq[q[1]] = 1
        elif q[0] == 2:
            if q[1] in arr:
                arr.remove(q[1])
                freq[q[1]] -= 1
        else:
            found = False
            for k,v in freq.items():
                if v == q[1]:
                    found = True
                    break
            if found:
                output.append(1)
            else:
                output.append(0)
            
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

