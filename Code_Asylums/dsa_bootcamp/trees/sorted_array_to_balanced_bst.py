# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return None
        mid=len(A)//2
        t=TreeNode(A[mid])
        t.left=t.right=TreeNode(-1)
        t.left=self.sortedArrayToBST(A[0:mid])
        t.right=self.sortedArrayToBST(A[mid+1:])
        return t
