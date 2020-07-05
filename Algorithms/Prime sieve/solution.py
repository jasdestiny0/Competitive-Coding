def seive(n):
    primeList = []
    primes = [0]*(n+1)
    for i in range(3,n+1,2):
        primes[i] = 1

    primes[2] = 1

    for i in range(n+1):
        if primes[i] == 1:
            for j in range(i*i,n+1,i):
                primes[j] = 0
            primeList.append(i)
    return primeList
    



def main():
    n = int(input())
    primeList = seive(n)
    print(primeList)

if __name__ == "__main__":
    main()
    
