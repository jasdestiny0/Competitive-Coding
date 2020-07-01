""" 
    Q)Given an array of size n with 0s and 1s , flip at most k 0s to get the longest possible subarray of 1s.
        Input Format
            First Line : n, size of array and k Second Line : n space separated numbers (0s or 1s)
        Constraints
            n <= 10^5 0 <= k <= n
        Output Format
            First Line : Size of subarray Second Line : Array after flipping k 0s

        Sample Input
            10 2
            1 0 0 1 0 1 0 1 0 1
        Sample Output
            5
            1 0 0 1 1 1 1 1 0 1
"""


def maxFlip(arr,n,k,l,r):
    zeroCount = 0
    maxOne = -1
    tempMax = 0
    i,j = 0, 0
    while(l <= r and r < n):
        if arr[r] == 0:
            zeroCount += 1
            while(zeroCount > k):
                if arr[l] == 0:
                    zeroCount -= 1
                l += 1
            
            
        
        tempMax = r-l+1

        if tempMax > maxOne:
            maxOne = tempMax
            i = l
            j = r


        r += 1

    return arr,i,j

n,k = map(int,input().split())
arr = list(map(int,input().split()))

lst,i,j= maxFlip(arr,n,k,0,0)

print(j-i+1)
for x in range(i,j+1):
    arr[x] = 1
for ele in arr:
    print(ele,end = ' ')