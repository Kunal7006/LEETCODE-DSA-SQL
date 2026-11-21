class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom up
        t=[[0]*(n) for _ in range(m)]

        for i in range(m):
            t[i][0]=1
        
        for j in range(n):
            t[0][j]=1
        
        for i in range(1,m):
            for j in range(1,n):
                t[i][j]=t[i-1][j]+t[i][j-1]
        
        return t[m-1][n-1]