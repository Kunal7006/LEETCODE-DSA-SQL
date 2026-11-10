class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj ={}
        for vec in times:
            u = vec[0]
            v = vec[1]
            w=vec[2]

            if u not in adj:
                adj[u] = []

            adj[u].append([v, w])
        
        pq =[]
        result = [float('inf')]*(n+1)
        
        result[k]=0
        heapq.heappush(pq,(0,k))

        while pq:
            d = pq[0][0]
            node = pq[0][1]
            heapq.heappop(pq)

            for vec in adj.get(node, []):
                adjNode = vec[0]
                dist = vec[1]

                if d+dist <result[adjNode]:
                    result[adjNode]= d+dist
                    heapq.heappush(pq,(d+dist,adjNode))
        ans = float('-inf')
        for i in range(1,n+1):
            ans = max(ans,result[i])
        
        if ans == float('inf'):
            return -1
        return ans


