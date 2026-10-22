from collections import deque

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            n = len(q)

            for _ in range(n):
                temp = q.popleft()

                if temp.left is not None:
                    q.append(temp.left)

                if temp.right is not None:
                    q.append(temp.right)

            depth += 1

        return depth