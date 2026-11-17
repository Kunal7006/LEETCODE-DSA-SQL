class Solution:
    def rob(self, nums: list[int]) -> int:
        # bottom up approach
        n = len(nums)
        t=[0]*(n+1) # max stolen money till i house 
        t[0]=0 # 0 house
        t[1]=nums[0] # 1 house

        for i in range(2,n+1):
            t[i]=max(nums[i-1]+t[i-2],t[i-1])
        return t[n]
