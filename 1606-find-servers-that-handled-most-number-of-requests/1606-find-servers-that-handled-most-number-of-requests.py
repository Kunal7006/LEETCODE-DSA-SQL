class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        available_servers = SortedSet()

        for i in range(k):
            available_servers.add(i)

        busyServers = []

        countRequest = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busyServers and busyServers[0][0] <= time:
                server = heapq.heappop(busyServers)[1]
                available_servers.add(server)

            target = i % k

            if not available_servers:
                continue

            idx = available_servers.bisect_left(target)

            if idx == len(available_servers):
                idx = 0

            targetServer = available_servers[idx]

            available_servers.remove(targetServer)

            heapq.heappush(
                busyServers,
                (time + load[i], targetServer)
            )

            countRequest[targetServer] += 1

        maxNumberOfRequests = max(countRequest)

        result = []

        for i in range(k):
            if countRequest[i] == maxNumberOfRequests:
                result.append(i)

        return result