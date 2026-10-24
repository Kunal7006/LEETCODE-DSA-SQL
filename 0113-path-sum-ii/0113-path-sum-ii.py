# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,curSum,targetSum,temp,ans):
        if root == None:
            return
        curSum += root.val
        temp.append(root.val)
        if not root.left and not root.right:
            if curSum == targetSum:
                ans.append(temp.copy())
        self.dfs(root.left,curSum,targetSum,temp,ans)
        self.dfs(root.right,curSum,targetSum,temp,ans)

        temp.pop() # backtrack

    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans =[]
        temp =[]
        self.dfs(root,0,targetSum,temp,ans)
        return ans