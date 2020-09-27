class Solution:
    def tribonacci(self, n: int, hashmap={0:0,1:1,2:1}) -> int:
        if n in hashmap: 
            return hashmap[n]
        else:
            val=self.tribonacci(n-1,hashmap)+self.tribonacci(n-2,hashmap)+self.tribonacci(n-3,hashmap)
            hashmap[n]=val
            return hashmap[n]
        
