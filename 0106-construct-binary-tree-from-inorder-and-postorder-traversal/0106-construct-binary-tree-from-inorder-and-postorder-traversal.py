# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, postorder, inorder, start, end):
        if start > end:
            return None

        rootVal = postorder[self.idx]

        i = start
        for i in range(start, end + 1):
            if inorder[i] == rootVal:
                break

        self.idx -= 1

        root = TreeNode(rootVal)

        root.right = self.solve(postorder, inorder, i + 1, end)
        root.left = self.solve(postorder, inorder, start, i - 1)

        return root

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        n = len(postorder)
        self.idx = n - 1

        return self.solve(postorder, inorder, 0, n - 1)