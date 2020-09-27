class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        phone={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        solution=[""]
        solution=self.helper(phone, solution, 0, digits, len(digits))
        return solution
    
    def helper(self, phone, solution, index, digits, length):
        if index>=length:
            return solution
        current=phone[digits[index]]
        currentArray=[]
        for i in solution:
            for j in current:
                currentArray.append(i+j)
        solution=currentArray
        return self.helper(phone, solution, index+1, digits, length)
        
        
