import math as m
def retModifiedSoe(n):
    soe=[0 for i in range(0,n+1)]
    for i in range(1,n+1,1):
        for j in range(i, n+1, i):
            soe[j]+=1
    return soe      

def afs(testcases,arr):
    sieve=retModifiedSoe(max(arr))
    seq=[0,0]
    for i in range(2,max(arr)+1,1):
        seq.append(seq[-1]+sieve[i])
    solution=[]
    print(sieve)
    print(seq)
    for i in arr:
        solution.append(seq[i])
    return solution
    
print(afs(3,[3,4,5]))

