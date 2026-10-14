class Solution:
    def solve(self,nums,ans,index):
        if index>= len(nums):
            ans.append(nums.copy())
            return 
        
        for j in range(index,len(nums)):
            nums[j],nums[index]=nums[index],nums[j]
            self.solve(nums,ans,index+1)
            nums[j],nums[index]=nums[index],nums[j]
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans =[]
        index =0
        self.solve(nums,ans,index)
        return ans