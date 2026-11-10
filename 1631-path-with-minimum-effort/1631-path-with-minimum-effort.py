class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        m = len(heights)
        n = len(heights[0])

        pq=[]
        result =[[float('inf')]*n for _ in range(m)]

        def isSafe(x,y):
            return x>=0 and x<m and y>=0 and y<n
        
        result[0][0]=0
        heapq.heappush(pq,(0,(0,0)))

        while pq:
            diff = pq[0][0]
            coord = pq[0][1]
            heapq.heappop(pq)

            x = coord[0]
            y = coord[1]

            for dir in dirs:
                x_=x+dir[0]
                y_=y+dir[1]

                if isSafe(x_,y_):
                    absDiff = abs(heights[x][y]-heights[x_][y_])
                    maxDiff = max(diff,absDiff)

                    if result[x_][y_]>maxDiff:
                        result[x_][y_]=maxDiff
                        heapq.heappush(pq,(maxDiff,(x_,y_)))
        return result[m-1][n-1]
        
