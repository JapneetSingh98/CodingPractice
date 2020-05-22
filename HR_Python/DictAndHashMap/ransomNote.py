'''
#!/bin/python3

import math
import os
import random
import re
import sys
'''

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for word in note:
        if word not in magazine:
            print("No")
            return
        else:
            magazine.remove(word)
    print("Yes")

'''
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
'''
