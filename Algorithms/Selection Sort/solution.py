def selectionSort(array):
	length=len(array)
    for i in range(0,length-1,1):
		minimumIndex=i
		for j in range(i+1,length,1):
			if array[j]<array[minimumIndex]:
				minimumIndex=j
		array[minimumIndex],array[i]=array[i],array[minimumIndex]
	return array
