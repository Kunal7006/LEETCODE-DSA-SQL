class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        heap =[]

        for i in range(m):
            count =0
            for j in range(n):
                if mat[i][j]==1:
                    count+=1
            heapq.heappush(heap,(-count,-i))

            if len(heap)>k:
                heapq.heappop(heap)
        
        result =[]

        while heap:
            result.append(-heapq.heappop(heap)[1])
        
        return result[::-1]