class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(logs)
        logs.sort(key=lambda x: x[1])
        q= len(queries)
        result = [0]*q

        timeIndex=[0]*q
        for i in range(q):
            timeIndex[i]=[queries[i],i]
        
        timeIndex.sort()

        mp={}

        i=0
        j=0

        for time,idx in timeIndex:
            start=time-x
            end =time

            while j<m and logs[j][1]<=end:
                if logs[j][0] not in mp:
                    mp[logs[j][0]]=0
                mp[logs[j][0]]+=1
                j+=1
            
            while i<m and logs[i][1]<start:
                mp[logs[i][0]]-=1
                if mp[logs[i][0]]==0:
                    mp.pop(logs[i][0])
                i+=1
            
            result[idx]=n-len(mp)
        return result