class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<vector<char>> grid(m,vector<char>(n,'#'));

        int i =0;
        int j =0;
        while(j<n){
            grid[i][j]='.';
            j++;
        }
        i=0;
        j = n-1;
        while(i<m){
            grid[i][j]='.';
            i++;
        }

        vector<string> ans;
        
        for(int i =0;i<m;i++){
            string s ="";
            for(int j =0;j<n;j++){
                s+= grid[i][j];
            }
            ans.push_back(s);
        }

        return ans;
    }
};