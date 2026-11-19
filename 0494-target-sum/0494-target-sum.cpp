class Solution {
public:
    int S;
    int solve(vector<int>& nums,int n,int currSum, int target,vector<vector<int>>& t){
        if(n<0){
           if(currSum==target) return 1;
           else return 0;
        }
        if(t[n][currSum+S]!=-1){
            return t[n][currSum+S];
        }
        int plus = solve(nums,n-1,currSum+nums[n],target,t);
        int minus = solve(nums,n-1,currSum-nums[n],target,t);

        return t[n][currSum+S] = plus + minus;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        S = accumulate(nums.begin(),nums.end(),0);
        vector<vector<int>> t(n+1,vector<int>(2*S+1,-1));
        return solve(nums,n-1,0,target,t);
    }
};