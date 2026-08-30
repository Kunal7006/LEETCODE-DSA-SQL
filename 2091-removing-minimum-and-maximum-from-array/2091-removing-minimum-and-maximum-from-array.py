class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return 1
        
        minIndex = 0
        maxIndex = 0

        for i in range(n):
            if nums[i]<nums[minIndex]:
                minIndex = i
            
            if nums[i]>nums[maxIndex]:
                maxIndex = i
            
        left = min(minIndex,maxIndex)
        right = max(minIndex,maxIndex)

        fromFront = right+1
        fromBack = n-left
        fromBoth = (left +1)+(n-right)

        return min(fromFront,fromBack,fromBoth)