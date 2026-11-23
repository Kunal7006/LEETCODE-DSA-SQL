class Solution {
public:
    int t[103][103];
    int solve(vector<int>& cuts,int l,int r){
        if(r-l<2){
            return 0;
        }
        if(t[l][r]!=-1){
            return t[l][r];
        }

        int result = INT_MAX;

        for(int index = l+1;index<=r-1;index++){
            int cost = cuts[r]-cuts[l] +solve(cuts,l,index)+solve(cuts,index,r);
            result = min(result,cost);
        }

        return t[l][r]=result;
    }
    int minCost(int n, vector<int>& cuts) {
        sort(cuts.begin(),cuts.end());
        cuts.insert(cuts.begin(),0); // 0->starting point of stick
        cuts.push_back(n); // n ->ending point of stick 

        //length of stick = cuts[r]-cults[l]
        memset(t,-1,sizeof(t));

        return solve(cuts,0,cuts.size()-1);
    }
};