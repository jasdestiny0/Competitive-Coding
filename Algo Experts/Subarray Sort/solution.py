def subarraySort(array):
  maxEndingIndex=-1
	startIndex=-1
	localMinima=float("inf")
	localMaxima=float("-inf")
	lengthOfArray=len(array)
	for i in range(lengthOfArray):
		if array[i]<localMaxima:
			maxEndingIndex=i
			if array[i]<localMinima:
				localMinima=array[i]	
		else:
			localMaxima=array[i]
	for i in range(0,lengthOfArray,1):
		if array[i]>=localMinima:
			startIndex=i
			break
	return [startIndex,maxEndingIndex]
			
		
