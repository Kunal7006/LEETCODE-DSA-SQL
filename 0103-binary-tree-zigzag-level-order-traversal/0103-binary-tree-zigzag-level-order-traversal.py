# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        if root == None:
            return ans
        q = deque()
        q.append(root)
        leftToRight = True

        while q:
            size = len(q)
            row = []
            for i in range(size):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                row.append(node.val)
            if not leftToRight:
                row.reverse()
                ans.append(row)
            else:
                ans.append(row)
            leftToRight = not leftToRight
        return ans
