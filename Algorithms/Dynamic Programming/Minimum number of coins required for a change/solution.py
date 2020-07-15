def minNumberOfCoinsForChange(n, denoms):
    l=[float("inf") for x in range(n+1)]
	l[0]=0
	for d in denoms:
		for i in range(n+1):
			if d<=i:
				l[i]=min(l[i], l[i-d]+1)

	return l[n] if l[n]!=float("inf") else -1
