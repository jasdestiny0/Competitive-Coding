def bubbleSort(array):
    length=len(array)
	for i in range(0,length,1):
		sorted=True
		for j in range(0,length-1-i,1):
			if array[j]>array[j+1]:
				array[j],array[j+1]=array[j+1],array[j]
				sorted=False
		if sorted:
			return array
	return array
