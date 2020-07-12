def hasSingleCycle(array):
    length=len(array)
	count=0
	index=0
	while count<length:
		if index==0 and count!=0:
			return False
		count+=1
		index+=array[index]
		index%=length
	return index==0
			
		
		
	
