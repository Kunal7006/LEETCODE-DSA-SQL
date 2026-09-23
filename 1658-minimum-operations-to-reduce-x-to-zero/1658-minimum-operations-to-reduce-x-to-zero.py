class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        l=0
        r=0

        sum =0
        total =0

        for i in range(n):
            total += nums[i]
        
        if x>total:
            return -1
        
        if x== total:
            return n
        
        target = total -x
        ans = float('inf')

        while r<n:
            sum += nums[r]

            while sum > target:
                sum-= nums[l]
                l+=1
            
            if sum == target:
                ans = min(ans,l+n-1-r)

            r+=1
        
        if ans == float('inf'):
            return -1
        return ans