class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)

        minSum = float('inf')
        maxSum = float('-inf')

        sum =0
        for i in range(n):
            sum+=nums[i]
            if sum <0:
                sum =0
            maxSum = max(maxSum , sum)
        
        sum =0

        for i in range(n):
            sum+=nums[i]
            if sum>0:
                sum =0
            minSum = min(minSum , sum)
        
        return max(abs(maxSum),abs(minSum))