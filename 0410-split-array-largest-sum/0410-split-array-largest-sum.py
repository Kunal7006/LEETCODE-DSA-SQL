class Solution:
    def countSubarray(self,nums,mid):
        count =1
        sum = 0
        for x in nums:
            if sum + x <=mid:
                sum += x
            else:
                count+=1
                sum = x
        return count

    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low)//2

            count = self.countSubarray(nums,mid)
            if count >k:
                low = mid +1
            else:
                high = mid -1
        return low