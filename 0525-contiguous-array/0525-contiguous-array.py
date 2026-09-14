class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxLength =0
        sum =0
        mp={}
        mp[0]=-1

        for i in range(n):
            if nums[i]==0:
                sum +=-1
            else:
                sum+=nums[i]
            
            if sum in mp:
                maxLength = max(maxLength,i-mp[sum])
            if sum not in mp:
                mp[sum]=i
        return maxLength