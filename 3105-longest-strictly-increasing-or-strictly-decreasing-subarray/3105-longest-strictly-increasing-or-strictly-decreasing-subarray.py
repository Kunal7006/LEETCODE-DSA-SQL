class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxLength =1
        i=0
        j=1

        while j<n:
            if nums[j]>nums[j-1]:
                maxLength = max(maxLength,j-i+1)
                j+=1
            else:
                i=j
                j=i+1
        
        i=0
        j=1

        while j<n:
            if nums[j]<nums[j-1]:
                maxLength = max(maxLength,j-i+1)
                j+=1
            else:
                i=j
                j=i+1
        return maxLength