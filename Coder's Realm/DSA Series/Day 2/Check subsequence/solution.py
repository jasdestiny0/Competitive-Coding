class Solution(object):
    def isSubsequence(self, s, t):
        indexS=0
        indexT=0
        while indexS<len(s) and indexT<len(t):
            if s[indexS]==t[indexT]:
                indexS+=1
            indexT+=1
    
        return len(s)==indexS
        
