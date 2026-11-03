class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        maxVal = max(nums)
        ans =0

        for num in nums:
            ans += abs(maxVal-num)
        return ans
