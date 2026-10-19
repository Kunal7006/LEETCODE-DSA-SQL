class Solution:
    def firstOccurence(self,nums,target):
        n = len(nums)
        low =0
        high = n-1
        ans =-1
        while low<=high:
            mid = low+(high-low)//2

            if nums[mid]==target:
                ans = mid
                high = mid-1
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return ans
    def lastOccurence(self,nums,target):
        n = len(nums)
        low =0
        high = n-1
        ans =-1
        while low<=high:
            mid = low+(high-low)//2

            if nums[mid]==target:
                ans = mid
                low = mid+1
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return ans
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans =[]
        nums.sort()
        first = self.firstOccurence(nums,target)
        last = self.lastOccurence(nums,target)

        if first!=-1:
            for i in range(first,last+1):
                ans.append(i)
        return ans