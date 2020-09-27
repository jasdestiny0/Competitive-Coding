# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("inf"),float("-inf"))
    
    def helper(self,n,maxi, mini):
        if n==None:
            return True
        
        if n.val>=maxi or n.val<=mini:
            return False
        
        return self.helper(n.left, n.val, mini) and self.helper(n.right, maxi, n.val)
