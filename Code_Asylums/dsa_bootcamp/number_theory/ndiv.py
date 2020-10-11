import math as m
def retModifiedSoe(n):
    soe=[0 for i in range(0,n+1)]
    for i in range(1,int((n+1)/2)+1,1):
        for j in range(i, n+1, i):
            soe[j]+=1
    return soe

def ndiv(a,b,n):
    sieve=retModifiedSoe(b)
    count=0
    for i in range(a,b+1,1):
        if sieve[i]==n:
            count+=1
    return count, sieve[1:]

print(ndiv(1,7,2))

