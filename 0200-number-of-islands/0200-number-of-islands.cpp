class Solution {
public:
    int m,n;
    bool dfs(vector<vector<char>>& grid,int r,int c){
        if(r>=m || r<0 || c>=n || c<0){
            return true;
        }
        if(grid[r][c]=='0'){
            return true;
        }
        grid[r][c]='0';

        bool left = dfs(grid,r,c-1);
        bool right = dfs(grid,r,c+1);
        bool up = dfs(grid,r-1,c);
        bool down = dfs(grid,r+1,c);

        return left && right && up && down;
    }
    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();

        int count =0;

        for(int i=0;i<m;i++){
            for(int j =0;j<n;j++){
                if(grid[i][j]=='1'){
                    if(dfs(grid,i,j)==true){
                        count++;
                    }
                }
            }
        }
        return count;
    }
};