def maxSubsetSumNoAdjacent(array):
    if len(array)==0:
		return 0
	
	first=max(array[0:2])
	second=array[0]
	for i in range(2,len(array),1):
		temp=first
		first=max(second+array[i],first)
		second=temp
	return first
		
		
