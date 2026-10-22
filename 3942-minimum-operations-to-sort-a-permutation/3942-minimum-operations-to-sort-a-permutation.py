class Solution:
    def solve(self,nums):
        n = len(nums)

        v=nums.copy()

        for num in nums:
            v.append(num)
        count =1

        for i in range(1,len(v)):
            if v[i]<v[i-1]:
                count =1
            else:
                count+=1

                if count == n:
                    return i + 1 -n
        
        count =1
        for i in range(1,len(v)):
            if v[i]>v[i-1]:
                count =1
            else:
                count+=1

                if count == n:
                    return i + 2 -n
        return 10**9

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        ans = self.solve(nums)

        nums=nums[::-1]

        ans = min(ans,self.solve(nums)+1)

        if ans == 10**9:
            return -1
        return ans