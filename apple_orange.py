# -*- coding: utf-8 -*-
"""apple_orange.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10_37WaJZfSHjj0IU5qd1GTen3l1c16Pp
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apple = toatal_orange = 0
    for i in range(len(apples)):
        if s<= a + apples[i] <=t:
            total_apple += 1
    for i in range(len(oranges)):
        if s<= b+ oranges[i] <= t:
            # Write your code here
            toatal_orange +=1
    print(total_apple)
    print(toatal_orange)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)