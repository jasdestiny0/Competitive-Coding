def waterArea(array):
	newhigh=0
	volume=0
	
	for i in range(0,len(array),1):
		if array[i]>newhigh:
			newhigh=array[i]
			newhighpos=i
		volume+=newhigh-array[i]
	
	oldhigh=newhigh
	newhigh=0

	for i in range(len(array)-1, -1,-1):
		if array[i]>newhigh:
			newhigh=array[i]
			newhighpos=i
		volume-=(oldhigh-newhigh)
		
	return volume
		
		
		
	
			
			
		
		
		
