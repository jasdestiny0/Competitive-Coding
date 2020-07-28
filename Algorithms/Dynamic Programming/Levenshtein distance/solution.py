def levenshteinDistance(str1, str2):
	dp=[[j for j in range(len(str1)+1)] for i in range(len(str2)+1)]
	for i in range(0,len(str2)+1,1):
		dp[i][0]=i
	for i in range(1,len(str2)+1):
		for j in range(1, len(str1)+1):
			if str2[i-1]==str1[j-1]:
				dp[i][j]=dp[i-1][j-1]
			else:
				dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
	return dp[-1][-1]
			
	 	
	
