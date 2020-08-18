#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(crew_id, job_id):
    cs=sorted(crew_id)
    js=sorted(job_id)

    cost=0
    for i in range(len(cs)):
        cost+=abs(cs[i]-js[i])

    return cost
if __name__ == '__main__':
