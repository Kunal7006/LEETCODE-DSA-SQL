class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum =0
        count =0
        mp={}
        mp[0]=1

        for i in range(n):
            sum += nums[i]
            rem = sum % k

            if rem in mp:
                count += mp[rem]
            if rem not in mp:
                mp[rem]=0
            mp[rem]+=1
        return count