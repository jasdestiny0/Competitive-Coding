def countPairs(numbers,k):
    seenMap={}
    for i in numbers:
        seenMap[i+k]=i
    solutionMap={}
    for i in numbers:
        if i in seenMap:
            solutionMap[i]=True
    return len(solutionMap)
print(countPairs([1,2,3,4,5,6],2))
        
