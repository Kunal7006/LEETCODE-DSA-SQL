# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,curSum,targetSum):
        if root == None:
            return False
        
        curSum += root.val
        if not root.left and not root.right:
            return curSum == targetSum
        return self.dfs(root.left,curSum,targetSum) or self.dfs(root.right,curSum,targetSum)

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        return self.dfs(root,0,targetSum)