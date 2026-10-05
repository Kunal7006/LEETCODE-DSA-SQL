class Solution:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp = {}
        n = len(nums)

        for x in nums:
            if x not in mp:
                mp[x]=0
            mp[x]+=1
        
        heap =[]

        for value,freq in mp.items():
            heapq.heappush(heap,(freq,value))

            if len(heap)>k:
                heapq.heappop(heap)
        
        ans = []

        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans