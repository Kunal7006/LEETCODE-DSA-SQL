# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self,root):
        if root == None:
            return 0
        return 1 + self.countNodes(root.left)+self.countNodes(root.right)

    def dfs(self,root,i,totalNodes):
        if root ==None:
            return True
        if i>totalNodes:
            return False
        return self.dfs(root.left,2*i,totalNodes) and self.dfs(root.right,2*i+1,totalNodes)

        
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        #dfs
        totalNodes = self.countNodes(root)

        i =1

        return self.dfs(root,i,totalNodes)