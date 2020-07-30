def knapsackProblem(items,capacity):
	sack=[[0 for i in range(capacity+1)] for j in range(len(items)+1)]
	for i in range(1,len(items)+1):
		currentWeight=items[i-1][1]
		currentValue=items[i-1][0]
		for j in range(0,capacity+1,1):
			if j-currentWeight>-1:
				sack[i][j]=max(sack[i-1][j-currentWeight]+currentValue,  sack[i-1][j])
			else:
				sack[i][j]=sack[i-1][j]
	return [0,[]]


	
	
	
			
    
