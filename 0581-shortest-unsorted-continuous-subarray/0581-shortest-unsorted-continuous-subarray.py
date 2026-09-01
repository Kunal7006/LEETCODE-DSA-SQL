class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left =0
        right = n-1

        while left < n-1:
            if nums[left]>nums[left+1]:
                break
            left+=1
        
        if left == n-1:
            return 0
        
        while right>0:
            if nums[right]<nums[right-1]:
                break
            right-=1
        
        maximum = float('-inf')
        minimum = float('inf')
        for i in range(left,right+1):
            if nums[i]<minimum:
                minimum = nums[i]
            if nums[i]>maximum:
                maximum = nums[i]
        
        while left>0 and nums[left-1]>minimum:
            left-=1
        while right<n-1 and nums[right+1]<maximum:
            right+=1
        
        return right -left +1