class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        v =[]
        v.append(target)
        v.append(0)
        stations.append(v)

        n = len(stations)
        ans =0
        heap =[]

        for i in range(n):
            if stations[i][0] > startFuel:
                while stations[i][0] > startFuel and heap:
                    k = -heapq.heappop(heap)
                    startFuel +=k
                    ans+=1
                if stations[i][0] > startFuel:
                    return -1
            heapq.heappush(heap,-stations[i][1])
        return ans