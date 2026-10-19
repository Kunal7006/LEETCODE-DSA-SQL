# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,l,r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        
        if l.val==r.val and self.check(l.left,r.right) and self.check(l.right,r.left):
            return True
        return False
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        
        return self.check(root.left,root.right)