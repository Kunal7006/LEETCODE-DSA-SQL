
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[False] * 1024 for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]] = True

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = [False] * 1024
                left = [False] * 1024

                if i > 0:
                    up = dp[i - 1][j]

                if j > 0:
                    left = dp[i][j - 1]

                combined = [up[k] or left[k] for k in range(1024)]

                for xorVal in range(1024):
                    if combined[xorVal]:
                        resultXorVal = xorVal ^ grid[i][j]
                        dp[i][j][resultXorVal] = True

        for xorVal in range(1024):
            if dp[m - 1][n - 1][xorVal]:
                return xorVal

        return -1
