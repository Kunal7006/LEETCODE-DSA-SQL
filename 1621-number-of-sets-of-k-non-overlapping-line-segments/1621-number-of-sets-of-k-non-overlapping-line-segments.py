class Solution:
    def numberOfSets(self, n: int, K: int) -> int:
        M = 10**9 + 7

        # dp[k][i]
        dp = [[0] * (n + 1) for _ in range(K + 1)]

        # Base case: k == 0
        for i in range(n):
            dp[0][i] = 1

        for k in range(1, K + 1):

            prevRowSum = [0] * (n + 1)

            # Calculate suffix sum of previous row
            for x in range(n - 1, -1, -1):
                prevRowSum[x] = (
                    prevRowSum[x + 1] + dp[k - 1][x]
                ) % M

            # Calculate current row
            for i in range(n - 1, -1, -1):

                take = prevRowSum[i + 1]

                skip = dp[k][i + 1] % M

                dp[k][i] = (take + skip) % M

        return dp[K][0]