class Solution {
public:
    unordered_map<string,int> mp;
    int solve(vector<int>& nums,int n,int currSum, int target){
        if(n<0){
           if(currSum==target) return 1;
           else return 0;
        }
        string key = to_string(n) + "_" + to_string(currSum);
        if(mp.count(key)){
            return mp[key];
        }
        int plus = solve(nums,n-1,currSum+nums[n],target);
        int minus = solve(nums,n-1,currSum-nums[n],target);

        return mp[key] = plus + minus;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        return solve(nums,n-1,0,target);
    }
};