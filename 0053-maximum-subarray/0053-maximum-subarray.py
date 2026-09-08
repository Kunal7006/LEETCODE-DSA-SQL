class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        sum =0

        for i in range(n):
            sum +=nums[i]

            ans = max(ans,sum)
            if sum < 0:
                sum =0
        
        return ans