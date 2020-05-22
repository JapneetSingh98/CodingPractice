'''
#!/bin/python3

import math
import os
import random
import re
import sys
'''

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for letter in s1:
        if letter in s2:
            return "YES"
    return "NO"

    
    ''' original idea, timed out
    
    if len(s1)==0 or len(s2)==0:
        return "NO"
    if len(s1) <= len(s2):
        if s1 in s2:
            return "YES"
        else:
            front = s1[0:len(s1)-1]
            back = s1[1:]

            if twoStrings(front, s2) is "YES" or twoStrings(back, s2) is "YES":
                return "YES"
            else:
                return "NO"
    else:
        if s2 in s1:
            return "YES"
        else:
            front = s2[0:len(s2)-1]
            back = s2[1:]

            if twoStrings(s1, front) is "YES" or twoStrings(s1, back) is "YES":
                return "YES"
            else:
                return "NO"
    '''


'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
'''