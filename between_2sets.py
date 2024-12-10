#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from math import gcd

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    l = reduce(lcm, a)  # Find the least common multiple (LCM) of array `a`
    g = reduce(gcd, b)  # Find the greatest common divisor (GCD) of array `b`
    
    s = 0
    for i in range(l, g + 1, l):  # Check multiples of `l` up to `g`
        if g % i == 0:  # If `i` is a factor of `g`
            s += 1
    return s

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
