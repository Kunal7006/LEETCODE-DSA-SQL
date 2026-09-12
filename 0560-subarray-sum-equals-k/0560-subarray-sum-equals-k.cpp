class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> mp;
        int preSum =0;
        int count = 0;

        mp[0]=1;

        for(int i=0;i<n;i++){
            preSum += nums[i];

            if(mp.find(preSum-k)!=mp.end()){
                count += mp[preSum-k];
            }

            mp[preSum]++;
        }
        return count;
    }
};