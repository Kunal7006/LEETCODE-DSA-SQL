class Solution {
public:
    int m,n;
    int delrow[4]={-1,0,1,0};
    int delcol[4]={0,1,0,-1};
    void dfs(int row,int col,vector<vector<int>>& visited,vector<vector<char>>& board){
        visited[row][col]=1;

        // check for top right bottom and left
        for(int i =0;i<4;i++){
            int nrow = row + delrow[i];
            int ncol = col + delcol[i];
            if(nrow>=0 && nrow<m && ncol >=0 && ncol<n && !visited[nrow][ncol] && board[nrow][ncol]=='O'){
                dfs(nrow,ncol,visited,board);
            }
        }

    }
    void solve(vector<vector<char>>& board) {
        m = board.size();
        n = board[0].size();

        vector<vector<int>> visited(m,vector<int>(n,0));
        //traverse first row and last row
        for(int j =0;j<n;j++){
            // first row
            if(!visited[0][j] && board[0][j]=='O'){
                dfs(0,j,visited,board);
            }
            //last row
            if(!visited[m-1][j] && board[m-1][j]=='O'){
                dfs(m-1,j,visited,board);
            }
        }

        // first and last col
        for(int i =0;i<m;i++){
            // first col
            if(!visited[i][0] && board[i][0]=='O'){
                dfs(i,0,visited,board);
            }
            //last col
            if(!visited[i][n-1] && board[i][n-1]=='O'){
                dfs(i,n-1,visited,board);
            }
        }

        for(int i =0;i<m;i++){
            for(int j =0;j<n;j++){
                if(!visited[i][j] && board[i][j]=='O'){
                    board[i][j]='X';
                }
            }
        }
        
    }
};