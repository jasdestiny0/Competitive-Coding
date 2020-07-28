def minNumberOfJumps(array):
	if len(array)<2:
		return 0
	jumps=1
	Range=array[0]
	nextRange=array[0]
	for i in range(1,len(array)-1):
		nextRange=max(nextRange,i+array[i])
		Range-=1
		if Range==0:
			Range=nextRange-i
			jumps+=1
		
	return jumps
	
		
	
    
