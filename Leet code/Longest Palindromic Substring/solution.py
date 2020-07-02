def longestPalindromicSubstring(string):
	i=0
	lengthOfString=len(string)
	maxLen=float("-inf")
	solution=""
	while i<=lengthOfString-1:
		j=lengthOfString-1
		length=0
		status=True
		x=i
		y=j
		while x<=y:
			if string[x]!=string[y]:
				j=y-1
				x=i
				status=False
			else:
				status=True
				x+=1
			y-=1
			
			
		if status and maxLen< (j-i+1):
			maxLen=(j-i)+1
			solution=string[i:j+1]
			
		i+=1
		
	return solution
			
				
		
		
	
			
