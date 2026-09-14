class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        int maxLength = 0;
        int sum =0;

        unordered_map<int,int> mp; // <sum-> index>
        mp[0]=-1;

        for(int i =0;i<n;i++){
            if(nums[i]==0){
                sum+=-1;
            }else{
                sum+=nums[i];
            }

            if(mp.find(sum)!=mp.end()){
                maxLength = max(maxLength,i- mp[sum]);
            }
            if(mp.find(sum)==mp.end()){
                mp[sum]=i;
            }
        }
        return maxLength;
    }
};