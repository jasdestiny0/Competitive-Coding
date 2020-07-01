# Question link:https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def binary(x,scores,ranks):
    i = 0
    j = len(scores)-1
    while(i<=j):
        mid = (i+j)//2
        score = scores[mid]
        if x == score:
            return ranks[mid]
        if x>score:
            j = mid-1
        else:
            i = mid+1
    if i>j and j>=len(scores):
        return ranks[i]+1
    if i>j and j<0:
        return 1
    if i>j:
        #print(i,x)
        return ranks[j]+1

def computeRanking(scores):
    ranks = [1]
    rank = 1
    n = len(scores)
    for i in range(1,n):
        if scores[i] == scores[i-1]:
            ranks.append(rank)
            
        else:
            rank += 1
            ranks.append(rank)
    return ranks

    

def climbingLeaderboard(scores, alice):
    res = []
    ranks = computeRanking(scores)
    #print(ranks)
    for x in alice:
        res.append(binary(x,scores,ranks))
    return res

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    for i in result:
        print(i)

