class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int minLength =INT_MAX;
        int sum =0;
        int left = 0;

        for(int i =0;i<n;i++){
            sum +=nums[i];

            if(sum>=target){
                
                while(sum>=target){
                    minLength = min(minLength,i-left+1);
                    sum -= nums[left];
                    left++;
                }
            }

        }
        if(minLength == INT_MAX){
            return 0;
        }
        return minLength;
    }
};