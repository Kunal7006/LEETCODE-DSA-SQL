class Solution:
    def firstOccurence(self,nums,n,target):
        l =0
        r=n-1
        ans = -1
        while l<=r:
            mid = l+(r-l)//2

            if target==nums[mid]:
                ans = mid
                r = mid -1
            elif target> nums[mid]:
                l = mid +1
            else:
                r = mid -1

        return ans

    def lastOccurence(self,nums,n,target):
        l=0
        r=n-1
        ans =-1
        
        while l<=r:
            mid = l +(r-l)//2

            if target== nums[mid]:
                ans = mid
                l = mid +1
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        return ans

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        ans=[]

        ans.append(self.firstOccurence(nums,n,target))
        ans.append(self.lastOccurence(nums,n,target))

        return ans