class Solution:
    def solve(self,nums,n,currSum,target,t):
        if n<0:
            if currSum == target: return 1
            else: return 0
        
        if t[n][currSum+self.S] != -1:
            return  t[n][currSum+self.S]
        
        plus = self.solve(nums,n-1,currSum+nums[n],target,t)
        minus = self.solve(nums,n-1,currSum-nums[n],target,t)

        t[n][currSum+self.S] = plus+minus
        return plus+minus

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        self.S=sum(nums)

        t =[[-1]*(2*self.S+1) for _ in range(n+1)]

        return self.solve(nums,n-1,0,target,t)