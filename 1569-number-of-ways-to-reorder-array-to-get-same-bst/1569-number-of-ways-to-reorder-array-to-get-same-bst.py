class Solution:
    def __init__(self):
        self.MOD = 10**9 +7
        self.PT =[]

    def solve(self,nums):
        n = len(nums)
        if n<3:
            return 1
        
        left_array =[]
        right_array =[]
        root = nums[0]


        for i in range(1,n):
            if nums[i]<root:
                left_array.append(nums[i])
            else:
                right_array.append(nums[i])
        
        x = self.solve(left_array) % self.MOD
        y = self.solve(right_array) % self.MOD
        z = self.PT[n-1][len(left_array)]

        return ((x*y) % self.MOD * z) % self.MOD

    def numOfWays(self, nums: list[int]) -> int:
        n = len(nums)
        self.PT = [[] for _ in range(n + 1)]

        for i in range(n+1):
            self.PT[i] = [1]*(i+1)

            for j in range(1,i):
                self.PT[i][j]=(self.PT[i-1][j] + self.PT[i-1][j-1]) % self.MOD
        
        return (self.solve(nums)-1) % self.MOD