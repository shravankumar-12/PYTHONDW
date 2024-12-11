#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(score):
    mincount = maxcount = 0
    minscore = maxscore =score[0]
    
    for i in range(1,len(score)):
        if minscore < score[i]:
            minscore = score[i]
            mincount +=1
        elif maxscore > score[i]:
            maxscore = score[i]
            maxcount +=1
    return mincount,maxcount
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
