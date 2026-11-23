class Solution {
public:
    int n;
    vector<vector<int>> t;
    int solve(vector<int>& prices,int index,int buy){
        if(index==n){
            return 0;
        }
        if(t[index][buy]!=-1){
            return t[index][buy];
        }
        if(buy){
            return t[index][buy]=max(-prices[index]+solve(prices,index+1,0),solve(prices,index+1,1));
        }else{
            return t[index][buy]=max(prices[index]+solve(prices,index+1,1),solve(prices,index+1,0));
        }
    }
    int maxProfit(vector<int>& prices) {
        n = prices.size();
        t.assign(n+1,vector<int>(2,-1));
        return solve(prices,0,1);
    }
};