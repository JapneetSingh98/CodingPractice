#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    trailing = []
    for i in range(len(expenditure)):
        trailing.sort()
        #print(trailing)
        if len(trailing) < d:
            trailing.append(expenditure[i])
        else:
            if d%2 == 1:
                if expenditure[i] >= 2*trailing[int(len(trailing)/2)]:
                    count += 1
            else:
                if expenditure[i] >= trailing[int(len(trailing)/2)]-1 + trailing[int(len(trailing)/2)]:
                    count += 1
            trailing.remove(expenditure[i-d])
            trailing.append(expenditure[i])
    return count
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
