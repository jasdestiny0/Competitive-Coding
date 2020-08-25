import math

class Solution:
    def isPalindrome(self, string: str) -> bool:
        s=[]
        for i in range(0,len(string),1):
            if string[i].isalpha():
                s.append(string[i].lower())
                
            elif string[i].isnumeric():
                s.append(string[i])
                
        #print(len(s))
        for i in range(0,math.floor(len(s)/2),1):
            #print(s[i],s[len(s)-i-1])
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
        
