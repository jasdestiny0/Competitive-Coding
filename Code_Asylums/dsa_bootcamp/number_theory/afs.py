import math as m
def retModifiedSoe(n):
    soe=[0 for i in range(0,n+1)]
    for i in range(1,n+1,1):
        for j in range(i, n+1, i):
            soe[j]+=1
    return soe      

def ndiv(a,b,n):
    sieve=retModifiedSoe(b)
    solution=[0 for ]
print(ndiv(1,7,2))

