def getPermutations(array):
	permutations=[]
	permuationsHelper(array, [], permutations)
	return permutations

def permuationsHelper(a,c,p):
	if not len(a) and len(c):
		p.append(c)
	
	else:
		for i in range(len(a)):
			n=a[:i]+a[i+1:]
			np=c+[a[i]]
			permuationsHelper(n,np,p)
	
			
			
