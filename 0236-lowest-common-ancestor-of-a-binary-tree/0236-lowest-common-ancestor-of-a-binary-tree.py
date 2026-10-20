# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        
        leftN = self.lowestCommonAncestor(root.left,p,q)
        rightN = self.lowestCommonAncestor(root.right,p,q)

        if leftN and rightN:
            return root
        if  leftN:
            return leftN
        return rightN