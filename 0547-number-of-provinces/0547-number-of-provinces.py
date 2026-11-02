class Solution:
    def dfs(self,isConnected,u,visited):
        visited[u]=True
        
        # find neighbours
        for v in range(self.n):
            if not visited[v] and isConnected[u][v]==1:
                self.dfs(isConnected,v,visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)

        visited=[False]*self.n

        count =0

        for i in range(self.n):
            if not visited[i]:
                self.dfs(isConnected,i,visited)
                count+=1
        return count