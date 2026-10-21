
class Solution:
    def __init__(self):
        self.n = 0

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.n = 0

        def inorder(root):
            if root is None:
                return None

            left = inorder(root.left)
            if left is not None:
                return left

            self.n += 1
            if self.n == k:
                return root.val

            return inorder(root.right)

        return inorder(root)
