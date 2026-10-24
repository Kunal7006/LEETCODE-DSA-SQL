class Solution:
    def dfs(self, root, num):
        if root is None:
            return 0

        num = num * 10 + root.val

        if not root.left and not root.right:
            return num

        left = self.dfs(root.left, num)
        right = self.dfs(root.right, num)

        return left + right

    def sumNumbers(self, root: TreeNode | None) -> int:
        return self.dfs(root, 0)