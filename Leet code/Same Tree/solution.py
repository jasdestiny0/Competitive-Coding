# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val!=q.val:
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
