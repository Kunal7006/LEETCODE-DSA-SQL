# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        ans =[]
        if root == None:
            return ans
        
        q = deque()
        q.append(root)

        while q:
            level =[]
            size = len(q)

            for i in range(size):
                node = q.popleft()
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        ans.reverse()
        return ans
            