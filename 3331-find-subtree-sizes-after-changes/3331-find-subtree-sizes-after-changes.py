class Solution:
    def __init__(self):
        self.adj={}
        self.resultSize=[]
        self.last =[]
    
    def dfs(self,currNode,s,parent):
        c = ord(s[currNode])-ord('a')
        nearestAncestor = self.last[c]

        self.last[c]=currNode

        for child in self.adj.get(currNode,[]):
            self.dfs(child,s,parent)
        
        self.last[c]=nearestAncestor

        if currNode!=0:
            newParent = parent[currNode]
            if nearestAncestor !=-1:
                newParent = nearestAncestor

            parent[currNode]=newParent

            self.resultSize[newParent]+=self.resultSize[currNode]

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        for i in range(1,n):
            u = parent[i]
            v = i
            if u not in self.adj:
                self.adj[u] =[]
            self.adj[u].append(i)
        
        self.resultSize =[1]*n
        self.last =[-1]*26

        self.dfs(0,s,parent)

        return self.resultSize

         
