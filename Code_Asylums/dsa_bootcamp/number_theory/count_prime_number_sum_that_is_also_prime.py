import math as m
def retSOE(n):
    soe=[True for i in range(0,n+1)]
    soe[0]=False
    soe[1]=False
    for i in range(2,n+1,1):
        if soe[i]:
            for j in range(pow(i,2),n,i):
                soe[j]=False
    return soe

def count_prime_numbers(l,r):
    soe=retSOE(r)
    solution=[]
    for i in range(l,r,1):
        if soe[i]:
            sumOfNum=0
            num=i
            while num!=0:
                sumOfNum+=(num%10)
                num//=10
            if soe[sumOfNum]:
                solution.append(i)
    return len(solution)
    
print(count_prime_numbers(1,10))
