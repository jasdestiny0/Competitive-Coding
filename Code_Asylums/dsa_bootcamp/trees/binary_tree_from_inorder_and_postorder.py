# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if len(A)==0:
            return None
        t=TreeNode(B[-1])
        posOfNode=A.index(B[-1])+1
        
        t.left=t.right=TreeNode(-1)
        t.left=self.buildTree(A[0:posOfNode-1], B[0:posOfNode-1])
        t.right=self.buildTree(A[posOfNode:], B[posOfNode-1:-1])
        return t
