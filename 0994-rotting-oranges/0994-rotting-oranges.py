class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        m = len(grid)
        n = len(grid[0])

        q = deque()
        freshOranges =0
        minutes =0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    freshOranges+=1
        
        if freshOranges ==0:
            return 0
        
        while q:
            N = len(q)
            while N:
                curr = q.popleft()
                i = curr[0]
                j = curr[1]

                for dir in directions:
                    new_i = i + dir[0]
                    new_j = j + dir[1]

                    if new_i>=0 and new_i<m and new_j>=0 and new_j<n and grid[new_i][new_j]==1:
                        grid[new_i][new_j] =2
                        q.append((new_i,new_j))
                        freshOranges-=1
                N-=1
            minutes+=1
        
        if freshOranges == 0:
            return  minutes-1 
        return -1
            

