class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        sum =0
        for i in range(n):
            sum +=nums[i]
        
        leftSum =0
        rightSum =sum 

        for i in range(n):
            leftSum += nums[i]

            if leftSum == rightSum:
                return i
            
            rightSum -= nums[i]
        return -1