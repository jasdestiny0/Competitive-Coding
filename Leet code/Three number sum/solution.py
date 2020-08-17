def threeNumberSum(array, targetSum):
	solution=[]
	array.sort()
	for i in range (0,len(array)-1,1):
		j=i+1;
		k=len(array)-1
		while j<k:
			sum1=array[i]+array[j]+array[k]
			if sum1==targetSum:
				solution.append([array[i],array[j],array[k]])
				j+=1
				k-=1
			elif sum1>targetSum:
				k-=1
			else:
				j+=1
	return solution
				
			
			
					
		
