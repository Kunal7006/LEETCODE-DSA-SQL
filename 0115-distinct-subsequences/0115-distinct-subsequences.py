
class Solution:
    def __init__(self):
        self.dp = [[-1] * 1001 for _ in range(1001)]

    def solve(self, s, t, m, n):
        if n == 0:
            self.dp[m][n] = 1
            return 1

        if m == 0:
            self.dp[m][n] = 0
            return 0

        if self.dp[m][n] != -1:
            return self.dp[m][n]

        if s[m - 1] == t[n - 1]:
            self.dp[m][n] = (
                self.solve(s, t, m - 1, n - 1) +
                self.solve(s, t, m - 1, n)
            )
        else:
            self.dp[m][n] = self.solve(s, t, m - 1, n)

        return self.dp[m][n]

    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)

        self.dp = [[-1] * (n + 1) for _ in range(m + 1)]

        return self.solve(s, t, m, n)

