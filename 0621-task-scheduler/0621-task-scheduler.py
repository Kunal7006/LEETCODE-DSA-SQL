class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        mp ={}

        for ch in tasks:
            if ch not in mp:
                mp[ch]=0
            mp[ch]+=1
        
        heap =[]
        time =0

        for char,freq in mp.items():
            heapq.heappush(heap,-freq)
        
        while heap:
            temp =[]
            for i in range(1,n+2):
                if heap:
                    freq = -heap[0]
                    heapq.heappop(heap)
                    freq-=1
                    temp.append(freq)
            
            for f in temp:
                if f>0:
                    heapq.heappush(heap,-f)
            
            if heap:
                time += n + 1
            else:
                time += len(temp)
        return time