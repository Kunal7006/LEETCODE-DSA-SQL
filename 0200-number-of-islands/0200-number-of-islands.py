from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    q = deque([(i, j)])
                    grid[i][j] = '0'

                    while q:
                        r, c = q.popleft()

                        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < m and 0 <= nc < n
                                    and grid[nr][nc] == '1'):
                                grid[nr][nc] = '0'
                                q.append((nr, nc))

        return count