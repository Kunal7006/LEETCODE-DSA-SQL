class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)

        freeServers =[]
        busyServers =[]

        for i in range(n):
            heapq.heappush(freeServers,(servers[i],i))
        
        result=[0]*m

        for i in range(m):
            while busyServers and busyServers[0][0]<=i:
                finTime = busyServers[0][0]
                wt= busyServers[0][1]
                idx = busyServers[0][2]
                heapq.heappop(busyServers)
                heapq.heappush(freeServers,(wt,idx))
            
            if not freeServers:
                finTime = busyServers[0][0]
                wt= busyServers[0][1]
                idx = busyServers[0][2]
                heapq.heappop(busyServers)
                result[i]=idx
                heapq.heappush(busyServers,(finTime+tasks[i],wt,idx))
            else:
                wt = freeServers[0][0]
                idx = freeServers[0][1]
                heapq.heappop(freeServers)
                result[i]=idx
                heapq.heappush(busyServers,(i+tasks[i],wt,idx))
        return result