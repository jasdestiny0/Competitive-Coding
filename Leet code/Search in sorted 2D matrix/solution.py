def searchInSortedMatrix(matrix, target):
	row=0
	column=len(matrix[0])-1
	while row<len(matrix) and column>-1:
		if matrix[row][column]>target:
			column-=1
		elif matrix[row][column]<target:
			row+=1
		else:
			return [row,column]
	return [-1,-1]
	
