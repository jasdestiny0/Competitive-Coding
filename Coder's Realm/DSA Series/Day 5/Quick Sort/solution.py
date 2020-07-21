def quickSort(array):
	doQS(array, 0, len(array)-1)
	return array

def doQS(array, startIdx, endIdx):
	if startIdx>=endIdx:
		return
	pivotIdx=startIdx
	leftIdx=pivotIdx+1
	rightIdx=endIdx
	while rightIdx>=leftIdx:
		if array[leftIdx]>array[pivotIdx] and array[rightIdx]<array[pivotIdx]:
			array[leftIdx],array[rightIdx]=array[rightIdx],array[leftIdx]
		if array[leftIdx]<=array[pivotIdx]:
			leftIdx+=1
		if array[rightIdx]>=array[pivotIdx]:
			rightIdx-=1
	array[pivotIdx],array[rightIdx]=array[rightIdx],array[pivotIdx]
	if rightIdx-1-startIdx<endIdx-(rightIdx+1):
		doQS(array,startIdx,rightIdx-1)
		doQS(array,rightIdx+1,endIdx)
	else:
		doQS(array,rightIdx+1,endIdx)
		doQS(array, startIdx,rightIdx-1)
	
