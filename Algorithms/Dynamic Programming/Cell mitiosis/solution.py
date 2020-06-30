"""
    Question : A container have one cell, a scientist wants to cultivate this cell to certain number N.
    At a time he can 
        1) double the cell count with the cost x,
        2) Increase the count by 1 with the cost y,
        3) Decrease the count by 1 with the cost z 

        Help him to cultivate with minimum cost

"""

def cellMitiosis(n,x,y,z):
    dp = dict()

    # Base case 
    dp[0] = 0
    dp[1] = 0

    #Remaining cases
    for i in range(2,n+1):
        ans = 0
        if i%2 == 0:
            ans = min((dp[i//2]+x),(dp[i-1]+y)) 
        else:
            ans = min((dp[i-1]+y),(dp[(i+1)//2]+x+z))
        
        dp[i] = ans
    
    return dp[n]




n,x,y,z = map(int,input().split())

ans = cellMitiosis(n,x,y,z)
print(ans)
