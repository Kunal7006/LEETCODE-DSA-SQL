class Solution {
public:
typedef pair<int,int> P;
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();

        priority_queue<P> pq;

        for(int i =0;i<m;i++){
            int count =0;
            for(int j =0;j<n;j++){
                if(mat[i][j]==1){
                    count++;
                }
            }
            pq.push({count,i});

            if(pq.size()>k){
                pq.pop();
            }
        }  

        vector<int> result;

        while(!pq.empty()){
            result.push_back(pq.top().second);
            pq.pop();
        } 
        reverse(result.begin(),result.end());
        return result;
    }
};