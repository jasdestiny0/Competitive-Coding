def soe(n):  
    prime = [True for i in range(n+1)] 
    number = 2
    while (number * number <= n): 
        if (prime[number] == True): 
            for i in range(number * number, n+1, number): 
                prime[i] = False
        number += 1

    pnoList=[]
    for number in range(2, n+1): 
        if prime[number]: 
            pnoList.append(number)

    return pnoList
print(soe(1000))
