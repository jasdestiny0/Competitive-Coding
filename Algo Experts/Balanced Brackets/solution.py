def balancedBrackets(string):
    stack=[1]
	count=0
	for i in string:
		if i=='[' or i=='(' or i=='{':
			stack.append(i)
			count+=1
		elif i==']' or i==')' or i=='}':
			if Type(stack[count])!=Type(i):
				return False
			else:
				stack.pop()
				count-=1
	
	if count!=0:
		return False
	return True
		
def Type(s):
	if s=='[' or s==']':
		return 1
	elif s=='{' or s=='}':
		return 2
	elif s=='(' or s==')':
		return 3
	return 4
