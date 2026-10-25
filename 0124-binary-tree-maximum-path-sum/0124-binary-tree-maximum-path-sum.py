# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root == None:
            return 0
        l = self.solve(root.left)
        r = self.solve(root.right)

        niche_hi_mila_acha = l + r + root.val
        koi_ek_acha = max(l,r)+root.val
        only_root_acha = root.val

        self.maxSum = max(self.maxSum,niche_hi_mila_acha,koi_ek_acha,only_root_acha)

        return max(koi_ek_acha,only_root_acha)
        
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxSum = float('-inf')
        self.solve(root)
        return self.maxSum