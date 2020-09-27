# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        self.findSol(root,list1)
        return list1
        
    def findSol(self,root,list1):
        if root!=None:
            if root.left!=None:
                self.findSol(root.left,list1)
        if root!=None:
            list1.append(root.val)
        if root!=None:
            if root.right!=None:
                self.findSol(root.right,list1)
