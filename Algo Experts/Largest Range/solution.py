def largestRange(array):
    numberList={x:True for x in array}
	checkList={x:True for x in array}
	nextNumber={}
	prevNumber={}
	x=0
	y=0
	maxLen=0
	for i in array:
		try:
			if numberList[i+1]:
				nextNumber[i]=i+1
		except:
			nextNumber[i]=i
		
		try:
			if numberList[i-1]:
				prevNumber[i]=i-1
		except:
			prevNumber[i]=i
		
	
	for i in array:
		if checkList[i]:
			left=i
			right=i
			while prevNumber[left]!=left:
				checkList[left]=False
				left=prevNumber[left]
				
			while nextNumber[right]!=right:
				checkList[right]=False
				right=nextNumber[right]
			if right-left+1>maxLen:
				maxLen=right-left+1
				x=left
				y=right
	return [x,y]
			
