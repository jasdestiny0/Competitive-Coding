def solution(arr):
    finalArray=[]
    doScheduling(0,arr,[],[],finalArray)
    diffArray=[]
    for i in finalArray:
        diffArray.append(abs(sum(i[0])-sum(i[1])))
    mini=min(diffArray)
    index=diffArray.index(mini)
    return finalArray[index]

def doScheduling(index,arr,a,b,finalArray):
    if index==len(arr):
        finalArray.append([a,b])
        return 
    
    doScheduling(index+1,arr,a+[arr[index]],b,finalArray)
    doScheduling(index+1,arr,a,b+[arr[index]],finalArray)

print(solution([i for i in range(1,18,1)]))
    
    
