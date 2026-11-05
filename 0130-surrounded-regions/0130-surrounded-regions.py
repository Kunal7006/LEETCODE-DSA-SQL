class Solution:
    def __init__(self):
        self.delrow =[-1,0,1,0]
        self.delcol=[0,1,0,-1]
    def dfs(self,row,col,visited,board):
        visited[row][col]=1
        for i in range(4):
            nrow = row + self.delrow[i]
            ncol = col + self.delcol[i]
            if nrow>=0 and nrow<self.m and ncol>=0 and ncol<self.n and not visited[nrow][ncol] and board[nrow][ncol]=='O':
                self.dfs(nrow,ncol,visited,board)
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m= len(board)
        self.n= len(board[0])

        visited =[[0]*self.n for _ in range(self.m)]

        for j in range(self.n):
            if not visited[0][j] and board[0][j]=='O':
                self.dfs(0,j,visited,board)
            if not visited[self.m-1][j] and board[self.m-1][j]=='O':
                self.dfs(self.m-1,j,visited,board)
        for i in range(self.m):
            if not visited[i][0] and board[i][0]=='O':
                self.dfs(i,0,visited,board)
            if not visited[i][self.n-1] and board[i][self.n-1]=='O':
                self.dfs(i,self.n-1,visited,board)
        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j] and board[i][j]=='O':
                    board[i][j]='X'


        