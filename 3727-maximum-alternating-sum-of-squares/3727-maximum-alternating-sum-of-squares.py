class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        temp=[]

        for num in nums:
            temp.append(abs(num))
        temp.sort()

        low =0
        high = n-1
        ans =0

        while low<high:
            ans += temp[high]**2 - temp[low]**2
            low+=1
            high-=1
        if n%2==1:
            ans += temp[low]**2
        return ans
