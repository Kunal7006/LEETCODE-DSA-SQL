class Solution:

    def solve(self, s, n, index, count):

        if count < 0:
            return False

        if index == n:
            return count == 0

        if self.dp[index][count] != -1:
            return self.dp[index][count]

        if s[index] == '(':
            self.dp[index][count] = self.solve(
                s, n, index + 1, count + 1
            )

        elif s[index] == ')':
            self.dp[index][count] = self.solve(
                s, n, index + 1, count - 1
            )

        else:
            # '*'
            self.dp[index][count] = (
                self.solve(s, n, index + 1, count + 1) or
                self.solve(s, n, index + 1, count - 1) or
                self.solve(s, n, index + 1, count)
            )

        return self.dp[index][count]

    def checkValidString(self, s: str) -> bool:

        n = len(s)

        self.dp = [[-1] * (n + 1) for _ in range(n)]

        return self.solve(s, n, 0, 0)