class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)

        m = len(cuts)

        t = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for l in range(m - length):
                r = l + length

                t[l][r] = float('inf')

                for index in range(l + 1, r):
                    cost = (
                        cuts[r] - cuts[l]
                        + t[l][index]
                        + t[index][r]
                    )

                    t[l][r] = min(t[l][r], cost)

        return t[0][m - 1]