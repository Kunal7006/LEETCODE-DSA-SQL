class Solution:
    def checkBipartiteBFS(self,graph,curr,color,currColor):
        q = deque()
        q.append(curr)
        color[curr]=currColor

        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v]==color[u]:
                    return False
                elif color[v]==-1:
                    color[v]= 1- color[u]
                    q.append(v)
        return True
    def isBipartite(self, graph: list[list[int]]) -> bool:
        V = len(graph)

        color = [-1]*V

        for i in range(V):
            if color[i]==-1:
                if self.checkBipartiteBFS(graph,i,color,1)==False:
                    return False
        return True