class Solution:
    def __init__(self):
        self.M = 10**9 + 7
        self.dp = [-1] * 2001
        self.prev = []

    def solve(self, n):
        if n == 0:
            return 1

        if self.dp[n] != -1:
            return self.dp[n]

        total = (2 * self.solve(n - 1)) % self.M

        if self.prev[n] != 0:
            duplicates = self.solve(self.prev[n] - 1)
            total = (total - duplicates + self.M) % self.M

        self.dp[n] = total
        return total

    def distinctSubseqII(self, s: str) -> int:
        n = len(s)

        self.dp = [-1] * 2001
        self.prev = [0] * (n + 1)

        lastSeen = [0] * 26

        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord('a')

            self.prev[i] = lastSeen[idx]
            lastSeen[idx] = i

        return (self.solve(n) - 1 + self.M) % self.M