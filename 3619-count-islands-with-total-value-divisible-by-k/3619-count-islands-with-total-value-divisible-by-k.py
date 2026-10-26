class Solution:
    def dfs(self, grid, r, c):
        if r >= self.m or r < 0 or c >= self.n or c < 0:
            return 0
        if grid[r][c] == 0:
            return 0
        sum = 0
        if grid[r][c] > 0:
            sum += grid[r][c]
        grid[r][c]=0
        
        left = self.dfs(grid, r, c - 1)
        right = self.dfs(grid, r, c + 1)
        up = self.dfs(grid, r - 1, c)
        down = self.dfs(grid, r + 1, c)

        return sum + left + right + up + down

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] > 0:
                    if self.dfs(grid, i, j) % k == 0:
                        count += 1
        return count
