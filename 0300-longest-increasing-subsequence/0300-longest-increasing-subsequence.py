
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        t = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for p in range(i - 1, -2, -1):

                take = 0
                if p == -1 or nums[i] > nums[p]:
                    take = 1 + t[i + 1][i + 1]

                skip = t[i + 1][p + 1]

                t[i][p + 1] = max(take, skip)

        return t[0][0]
