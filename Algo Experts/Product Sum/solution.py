# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array,level=1):
    solution=0
	for i in array:
		if type(i)==int:
			solution+=level*i
		else:
			solution+=level*productSum(i,level+1)
	return solution
