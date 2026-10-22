# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return 0
        leftH = self.height(root.left)
        if leftH == -1:
            return -1
        rightH = self.height(root.right)
        if rightH == -1:
            return - 1
        if abs(leftH - rightH) > 1:
            return -1
        return 1 + max(leftH, rightH)

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.height(root) != -1
