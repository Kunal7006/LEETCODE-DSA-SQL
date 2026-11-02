class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        minVal = min(nums)

        moves =0

        for num in nums:
            moves += num - minVal
        return moves