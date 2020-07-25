def quickSort(array):
	doQS(array,0,len(array)-1)
	return array

def doQS(array,l,e):
	if l>=e:
		return
	p=l
	l=l+1
	r=e
	while l<=r:
		if array[l]>array[p] and array[r]<array[p]:
			array[l],array[r]=array[r],array[l]
		elif array[l]<=array[p]:
			l+=1
		elif array[r]>=array[p]:
			r-=1
			
	array[p],array[r]=array[r],array[p]
	len1=r-p
	len2=e-r-1
	
	if len1<len2:
		doQS(array,p,r-1)
		doQS(array, r+1, e)
	else:
		doQS(array, r+1, e)
		doQS(array,p,r-1)
	
	
