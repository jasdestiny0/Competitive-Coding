def knapsackProblem(items,capacity):
	sack=[[0 for i in range(capacity+1)] for j in range(len(items)+1)]
	for i in range(1,len(items)+1):
		currentWeight=items[i-1][1]
		currentValue=items[i-1][0]
		for j in range(0,capacity+1,1):
			if j-currentWeight>-1:
				if sack[i-1][j-currentWeight]+currentValue<sack[i-1][j]:
					sack[i][j]=sack[i-1][j]
				else:
					sack[i][j]=sack[i-1][j-currentWeight]+currentValue
			else:
				sack[i][j]=sack[i-1][j]
	solution=getSolution(sack,items)
	return [sack[-1][-1],solution]

def getSolution(knapsackValues,items):
	sequence=[]
	i=len(knapsackValues)-1
	c=len(knapsackValues[0])-1
	while i>0:
		if knapsackValues[i][c]==knapsackValues[i-1][c]:
			i-=1
		else:
			sequence.append(i-1)
			c-=items[i-1][1]
		if c==0:
			break
	return list(reversed(sequence))


	
	
	
			
    
