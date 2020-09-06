class Solution:
    def maxSubArray(self, l: List[int]) -> int:
        if len(l)==0:
            return 0
        maxi=float("-inf")
        highestMaxi=float("-inf")
        for i in l:
            print(maxi)
            maxi=max(maxi+i,i)
            if highestMaxi<maxi:
                highestMaxi=maxi
        return highestMaxi
        
