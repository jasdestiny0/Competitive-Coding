#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    order=sorted(order)
    sum=0
    number=0
    broken=False
    for i in order:
        sum+=i
        number+=1
        if sum>k:
            broken=True
            break
    return number-1 if broken else number

if __name__ == '__main__':
