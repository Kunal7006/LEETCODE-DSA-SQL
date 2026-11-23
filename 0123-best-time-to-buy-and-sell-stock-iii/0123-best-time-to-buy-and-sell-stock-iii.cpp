class Solution {
public:
    int n;
    vector<vector<vector<int>>> t;
    int solve(vector<int>& prices,int i,int b,int txn){
        if(i==n || txn ==0){
            return 0;
        }

        if(t[i][b][txn]!=-1){
            return t[i][b][txn];
        }
        if(b){
            return t[i][b][txn]=max(-prices[i]+solve(prices,i+1,0,txn),solve(prices,i+1,1,txn));
        }else{
            return t[i][b][txn]=max(prices[i]+solve(prices,i+1,1,txn-1),solve(prices,i+1,0,txn));
        }
        
    }
    int maxProfit(vector<int>& prices) {
        n = prices.size();
        t.assign(n,vector<vector<int>>(2,vector<int>(3,-1)));
        return solve(prices,0,1,2);
    }
};