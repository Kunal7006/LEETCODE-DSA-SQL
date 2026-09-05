class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum =0
        minLength = float('inf')

        left = 0

        for i in range(n):
            sum += nums[i]

            while sum>=target:
                minLength = min(minLength,i-left+1)
                sum-= nums[left]
                left+=1
            
        if minLength == float('inf'):
            return 0
        return minLength