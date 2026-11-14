class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        prefix =[0]*(n+1)

        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        
        for i in range(n):
            for length in range(l,r+1):
                if i + length > n:
                    break
                sum = prefix[i+length]-prefix[i]

                if sum>0:
                    ans = min(ans,sum)
        
        return -1 if ans == float('inf') else ans
