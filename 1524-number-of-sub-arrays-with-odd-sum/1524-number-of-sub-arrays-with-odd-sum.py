class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        M = 10**9 + 7
        n = len(arr)
        odd =0
        even =1
        count =0

        prefix = [0]*n
        prefix[0]=arr[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + arr[i]
        
        for i in range(n):
            if prefix[i]%2==0:
                count = (count + odd) % M
                even+=1
            else:
                count = (count + even) % M
                odd+=1
        return count