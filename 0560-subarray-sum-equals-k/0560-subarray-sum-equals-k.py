class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp ={}
        preSum =0
        count =0

        mp[0]=1

        for i in range(n):
            preSum += nums[i]
            remove = preSum -k
            if remove in mp:
                count += mp[remove]
            if preSum in mp:
                mp[preSum]+=1
            else:
                mp[preSum]=1
        return count