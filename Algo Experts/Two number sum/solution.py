# Time O(n) Space O(n)

def twoNumberSum(array, targetSum):
    dict1={}
	for i in array:
		if targetSum-i in dict1:
			return [targetSum-i,i]
		dict1[i]=True
	return []
  
  # Time O(nlogn) Space O(1)
	
 def twoNumberSum(array, targetSum):
	array.sort()
	left=0
	right=len(array)-1
	while left<right:
		sum1=array[left]+array[right]
		if sum1==targetSum:
			return [array[left],array[right]]
		elif sum1<targetSum:
			left+=1
		elif sum1>targetSum:
			right-=1
	return []
			
	
	

	
