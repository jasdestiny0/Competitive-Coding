def numberOfWaysToMakeChange(n, denoms):
	l=[0 for i in range(n+1)]
	l[0]=1
	for d in denoms:
		for i in range(1,n+1):
			if d<=i:
				l[i]+=l[i-d]
	return l[n]
		
