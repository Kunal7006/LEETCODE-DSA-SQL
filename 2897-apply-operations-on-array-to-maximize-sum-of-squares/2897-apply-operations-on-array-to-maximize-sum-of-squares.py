class Solution:
    def __init__(self):
        self.MOD = 10**9 +7
    
    def maxSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0]*32

        for num in nums:
            for b in range(32):
                if num & (1<<b):
                    count[b]+=1
        
        result = 0

        while k:
            curr =0
            for b in range(32):
                if count[b]>0:
                    count[b]-=1

                    curr = (curr |(1<<b))
            result = (result + (curr * curr)) % self.MOD
            k-=1
        
        return result