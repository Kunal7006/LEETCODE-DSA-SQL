# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def height(self, root):
        if root == None:
            return 0
        leftH = self.height(root.left)
        rightH = self.height(root.right)

        self.diameter = max(self.diameter, leftH + rightH)
        return 1 + max(leftH, rightH)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter
