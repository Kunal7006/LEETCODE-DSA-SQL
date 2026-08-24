class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Calculate prefix sums
        prefix = stones[:]

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        # dp represents the maximum score difference
        dp = prefix[-1]

        # Process from right to left
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp