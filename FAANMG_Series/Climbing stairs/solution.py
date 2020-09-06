def numberOfWays(n):
        ways=[0 for i in range(n)]
        ways[0]=1
        ways[1]=2
        for i in range(2,n,1):
              ways[i]=ways[i-1]+ways[i-2]  
        return ways[n-1]

print(numberOfWays(4))
