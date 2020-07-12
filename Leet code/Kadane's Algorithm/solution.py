def kadanesAlgorithm(Array):
	MaxHere=Array[0]
	MaxSoFar=Array[0]
	for i in range(1,len(Array),1):
		Number=Array[i]
		MaxHere=max(Number,Number+MaxHere)
		MaxSoFar=max(MaxSoFar,MaxHere)
	return MaxSoFar
