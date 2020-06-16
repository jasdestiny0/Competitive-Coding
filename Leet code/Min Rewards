def minRewards(scores):
    reward=[1 for i in scores]
    length=len(scores)
    for i in range(1,length,1):
        if scores[i]>scores[i-1]:
            reward[i]=reward[i-1]+1
	for i in range(length-2,-1,-1):
        if scores[i]>scores[i+1]:
            reward[i]=max(reward[i+1]+1, reward[i])
    return sum(reward)
