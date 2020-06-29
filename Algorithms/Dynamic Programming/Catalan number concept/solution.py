"""
    Question: How many binary search trees can be formed from the N nodes numbered from 1 to N?

    Ans: The series formed in this question is otherwise called catalan numbers, so we can also obtain the answer using 
    the general term of the catalan series which is 2nCn/(n+1)
"""


dp = dict()

def noOfBinaryTrees(n:int)->int:
    if n==0 or n==1:
        return 1
    if dp.get(n) is not None:
        return dp[n]
    ans = 0
    for i in range(1,n+1):
        ans += ((noOfBinaryTrees(i-1)*(noOfBinaryTrees(n-i)))) 
    
    dp[n] = ans
    return ans


n = int(input())

print(noOfBinaryTrees(n))

