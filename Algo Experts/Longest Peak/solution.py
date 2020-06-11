def longestPeak(array):
	if len(array)<3:
		return 0
    peakLength=float("-inf")
    rightIndex=0
    leftIndex=0
    length=len(array)
    for i in range(1,length-1,1):
        isPeak=array[i-1]<array[i] and array[i]>array[i+1]
        
        if isPeak:
            leftIndex=i-1
			
            while leftIndex>0 and array[leftIndex-1]<array[leftIndex]:
                leftIndex-=1
            rightIndex=i+1
            while rightIndex<length-1 and array[rightIndex]>array[rightIndex+1]:
                rightIndex+=1
        
		if peakLength<rightIndex-leftIndex+1:
			peakLength=rightIndex-leftIndex+1
			
	if peakLength<3:
		return 0
		
    return peakLength
		
