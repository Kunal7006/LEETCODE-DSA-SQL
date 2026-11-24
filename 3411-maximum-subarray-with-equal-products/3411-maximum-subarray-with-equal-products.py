class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res =0

        for i in range(n):
            p=1
            g=0
            l=1
            for j in range(i,n):
                p *=nums[j]
                g = gcd(g,nums[j])
                l = lcm(l,nums[j])
                if p == l * g:
                    res = max(res,j-i+1)
            
        return res