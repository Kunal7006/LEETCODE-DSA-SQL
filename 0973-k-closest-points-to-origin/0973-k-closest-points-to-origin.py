class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        n = len(points)

        heap =[]

        for point in points:

            x = point[0]
            y = point[1]

            distance = x*x + y*y

            heapq.heappush(heap,(-distance,point))

            if len(heap)>k:
                heapq.heappop(heap)
        
        result=[]

        while heap:
            result.append(heapq.heappop(heap)[1])
        return result;