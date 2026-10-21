# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        if not root.left and not root.right:
            return 1
        
        if root.left:
            l = self.minDepth(root.left)
        else:
            l = float('inf')
        if root.right:
            r = self.minDepth(root.right)
        else:
            r = float('inf')
        return 1 + min(l,r)