#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    trail = []
    count = 0
    for i in range(len(expenditure)):
        print(trail)
        print(expenditure[i])
        if i < d:
            trail.append(expenditure[i])
        else:
            trail.sort()
            if len(trail) % 2 == 1:             # odd
                if expenditure[i] >= 2* trail[int(len(trail)/2)]:
                    count = count + 1
            else:
                if expenditure[i] >= trail[int(len(trail)/2)-1] + trail[int(len(trail)/2)]:
                    count = count + 1
            trail.remove(expenditure[i-d])
            trail.append(expenditure[i])
    return count
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

