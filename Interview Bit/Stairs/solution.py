class Solution:
    def climbStairs(self, n):
        if n==0:
            return 1
        arr=[1,2]
        for i in range(2,n+1):
            arr.append(arr[-1]+arr[-2])
        
        return arr[n-1]
