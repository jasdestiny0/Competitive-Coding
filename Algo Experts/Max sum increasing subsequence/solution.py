def maxSumIncreasingSubsequence(array):
	if len(array)==0:
		return 0
	sumArray=[array[0]]
	sequenceArray=[[array[0]]]
	for i in range(1,len(array)):
		maxVal=float("-inf")
		canUse=False
		for j in range(0,i):
			if array[j]<array[i] and sumArray[j]>=maxVal and sumArray[j]>0:
				maxIndex=j
				maxVal=sumArray[maxIndex]
				canUse=True
		if canUse:
			sumArray+=[array[i]+sumArray[maxIndex]]
			sequenceArray.append(sequenceArray[maxIndex]+[array[i]])
		else:
			sumArray+=[array[i]]
			sequenceArray.append([array[i]])
	ind=sumArray.index(max(sumArray))
	return [sumArray[ind],sequenceArray[ind]]
