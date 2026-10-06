class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap =[]

        for x in stones:
            heapq.heappush(heap,-x)

        while len(heap)>1:

            a = heap[0]
            heapq.heappop(heap)
            b = heap[0]
            heapq.heappop(heap)

            if abs(a-b)!=0:
                heapq.heappush(heap,-abs(a-b))
        
        if len(heap)==0:
            return 0
        return -heap[0]
