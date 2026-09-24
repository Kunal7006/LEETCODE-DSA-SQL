class Solution:
    def digitSum(self,n):
        sum =0
        while n:
            digit = n % 10
            sum += digit
            n = n // 10
        return sum
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            if self.digitSum(nums[i])==i:
                ans =i
                break
        return ans