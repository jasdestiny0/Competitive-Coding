def getNthFib(n):
	list1=[0,1]
	if n<3:
		return list1[n-1]
	
	for i in range(1,n,1):
		nextFib=list1[0]+list1[1]
		list1[0]=list1[1]
		list1[1]=nextFib
	
	return list1[0]
