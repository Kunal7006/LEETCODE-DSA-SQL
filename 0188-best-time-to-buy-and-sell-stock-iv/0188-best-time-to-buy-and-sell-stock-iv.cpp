class Solution {
public:
    int n;
    vector<vector<vector<int>>> t;
    int solve(vector<int>& prices,int i,int b,int k){
        if(i==n || k==0){
            return 0;
        }
        if(t[i][b][k]!=-1){
            return t[i][b][k];
        }
        if(b){
            return t[i][b][k]=max(-prices[i]+solve(prices,i+1,0,k),solve(prices,i+1,1,k));
        }else{
            return t[i][b][k]=max(prices[i]+solve(prices,i+1,1,k-1),solve(prices,i+1,0,k));
        }
    }
    int maxProfit(int k, vector<int>& prices) {
        n = prices.size();
        t.assign(n,vector<vector<int>>(2,vector<int>(k+1,-1)));
        return solve(prices,0,1,k);
    }
};