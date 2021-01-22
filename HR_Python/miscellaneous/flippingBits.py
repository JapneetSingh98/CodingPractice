#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    binary = str(bin(n))[2:]
    while len(binary) < 32:
        binary = '0' + binary
    flipped = "0b"
    for char in binary:
        if char == '1':
            flipped += '0'
        else:
            flipped += '1'
    print(flipped)
    return int(flipped,2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()