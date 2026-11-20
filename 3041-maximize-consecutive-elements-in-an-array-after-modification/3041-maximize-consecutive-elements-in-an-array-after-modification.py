
from bisect import bisect_left

class Solution:
    def __init__(self):
        self.n = 0
        self.memo = []

    def findMethod(self, nums, start, target):
        j = bisect_left(nums, target, start)

        if j < self.n and nums[j] == target:
            return j

        return -1

    def solve(self, i, inc, nums):
        if self.memo[i][inc] != -1:
            return self.memo[i][inc]

        currVal = nums[i] + inc  # inc -> 0/1

        length = 1

        # 1st option -> find currVal + 1
        j = self.findMethod(nums, i + 1, currVal + 1)

        if j != -1:
            length = max(length, 1 + self.solve(j, 0, nums))

        # 2nd option -> find currVal and increment by +1
        j = self.findMethod(nums, i + 1, currVal)

        if j != -1:
            length = max(length, 1 + self.solve(j, 1, nums))

        self.memo[i][inc] = length
        return length

    def maxSelectedElements(self, nums: list[int]) -> int:
        self.n = len(nums)

        nums.sort()

        self.memo = [[-1] * 2 for _ in range(self.n + 1)]

        result = 1

        for i in range(self.n):
            result = max(result, self.solve(i, 0, nums), self.solve(i, 1, nums))

        return result
