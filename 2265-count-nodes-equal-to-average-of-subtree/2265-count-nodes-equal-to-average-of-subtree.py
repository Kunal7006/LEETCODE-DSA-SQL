# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def dfs(node):
            if node is None:
                return (0, 0)   # (sum, count)

            # Get left subtree sum and count
            leftSum, leftCount = dfs(node.left)

            # Get right subtree sum and count
            rightSum, rightCount = dfs(node.right)

            # Current subtree sum and count
            totalSum = node.val + leftSum + rightSum
            totalCount = 1 + leftCount + rightCount

            # Calculate average
            average = totalSum // totalCount

            # Check if node value equals average
            if node.val == average:
                self.ans += 1

            return (totalSum, totalCount)

        dfs(root)

        return self.ans
        