class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)

        vec = []

        for i in range(n):
            vec.append([capital[i],profits[i]])
        
        vec.sort()

        i=0

        heap =[]

        while k:
            while i<n and vec[i][0]<=w:
                heapq.heappush(heap,-vec[i][1])
                i+=1
            if not heap:
                break
            w+= -heapq.heappop(heap)
            k-=1
        return w

