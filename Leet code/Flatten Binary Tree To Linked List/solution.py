# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l=[]
        self.getList(root, l)
        if root==None:
            return
        if root.left!=None:
            root.left=None
        n=root
        for i in l[1:]:
            n.right=TreeNode(i)
            n=n.right
        
    
    def getList(self, node, l):
        if node==None:
            return
        
        l.append(node.val)
        self.getList(node.left,l)
        self.getList(node.right,l)
