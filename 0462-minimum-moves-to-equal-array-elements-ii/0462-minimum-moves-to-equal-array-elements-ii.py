class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()
        mid = nums[n // 2]

        moves = 0

        for i in range(n // 2):
            moves += abs(nums[i] - mid)
            moves += abs(nums[n - i - 1] - mid)

        return moves