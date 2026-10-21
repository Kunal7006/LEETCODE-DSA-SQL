
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.vec = []

    def convert(self, root):
        if root is None:
            return

        self.convert(root.left)
        self.vec.append(root.val)
        self.convert(root.right)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.vec = []  # Reset for each function call
        self.convert(root)

        n = len(self.vec)
        i = 0
        j = n - 1

        while i < j:
            if self.vec[i] + self.vec[j] == k:
                return True
            elif self.vec[i] + self.vec[j] < k:
                i += 1
            else:
                j -= 1

        return False
