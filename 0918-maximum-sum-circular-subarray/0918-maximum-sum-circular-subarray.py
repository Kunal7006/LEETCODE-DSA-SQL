class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        totalSum =0

        for i in range(n):
            totalSum +=nums[i]
        
        minSum = float('inf')
        sum =0

        for i in range(n):
            sum += nums[i]

            minSum = min(minSum,sum)
            if sum >0:
                sum =0
        
        sum =0
        maxSum = float('-inf')

        for i in range(n):
            sum += nums[i]

            maxSum = max(maxSum,sum)
            if sum <0:
                sum =0
        
        if maxSum<0:
            return maxSum
        
        return max(maxSum,totalSum-minSum)