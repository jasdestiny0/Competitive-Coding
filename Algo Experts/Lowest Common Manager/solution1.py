# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        n=self.helper(root, p, q)
        return n.lowestManager
    
    def helper(self, node, nodeA, nodeB):
        if node==None:
            return solnNode(None, 0)
        
        n=0
        m=self.helper(node.left, nodeA, nodeB)
        o=self.helper(node.right, nodeA, nodeB)
        
        if node==nodeA or node==nodeB:
            n+=1 
            
        n+=m.count
        n+=o.count
        s=solnNode(node, n)
        
        if m.count==2:
            s.lowestManager=m.lowestManager
        elif o.count==2:
            s.lowestManager=o.lowestManager
            
        return s
            
        
        
        
class solnNode:
    def __init__(self, lowestManager, count):
        self.lowestManager=lowestManager
        self.count=count
        