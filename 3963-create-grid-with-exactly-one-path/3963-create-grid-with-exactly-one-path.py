class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid =[['#']*n for _ in range(m)]

        i =0
        j=0
        while j<n:
            grid[i][j]='.'
            j+=1
        
        i=0
        j=n-1
        while i<m:
            grid[i][j]='.'
            i+=1
        
        ans =[]

        for i in range(m):
            s=""
            for j in range(n):
                s+=grid[i][j]
            ans.append(s)
        
        return ans