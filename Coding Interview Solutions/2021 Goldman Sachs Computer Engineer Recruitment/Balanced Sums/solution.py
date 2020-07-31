def balancedSum(arr):
    sumOfArr=sum(arr)
    leftSum=0
    minPhase=float("inf")
    minPhaseSol=float("inf")
    index=float("inf")
    for i in range(1,len(arr),1):
        leftSum+=arr[i-1]
        rightSum=sumOfArr-leftSum-arr[i]
        phase=abs(rightSum-leftSum)
        
        if phase<minPhase:
            minPhase=phase
            minPhaseSol=arr[i]
            index=i
        elif phase==minPhaseSol:
            if arr[i]<minPhaseSol:
                minPhaseSol=arr[i]
                index=i  
    return index 

print(balancedSum([1,2,3,3]))
            
            
