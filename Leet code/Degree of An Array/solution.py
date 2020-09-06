class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count={}
        firstAppearance={}
        lastAppearance={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
                firstAppearance[nums[i]]=i
                lastAppearance[nums[i]]=i
            else:
                count[nums[i]]+=1
                lastAppearance[nums[i]]=i
        maxi=[]
        maxVal=0
        for i,j in count.items():
            if maxVal<j:
                maxVal=j
                maxi=[i]
            elif maxVal==j:
                maxi+=[i]
        
        shortest=float("inf")
        for i in maxi:
            diff=lastAppearance[i]-firstAppearance[i]+1
            if diff<shortest:
                shortest=diff
        return shortest
            
                
                
        
