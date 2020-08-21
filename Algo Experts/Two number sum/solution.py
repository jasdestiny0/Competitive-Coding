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
    dict1={}
    for i in array:
      if targetSum-i in dict1:
        return [targetSum-i,i]
      dict1[i]=True
    return []
