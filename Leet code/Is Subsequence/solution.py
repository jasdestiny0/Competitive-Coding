class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        sLen=len(s)
        tLen=len(t)
        sIndex=0
        tIndex=0
        while sIndex<sLen and tIndex<tLen:
            if s[sIndex]==t[tIndex]:
                tIndex+=1
            sIndex+=1
        return tLen==tIndex
