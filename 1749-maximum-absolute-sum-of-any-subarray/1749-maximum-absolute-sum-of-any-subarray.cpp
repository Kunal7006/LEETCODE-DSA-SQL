class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size();

        int minSum = INT_MAX;
        int maxSum = INT_MIN;
        int sum =0;
        

        for(int i =0;i<n;i++){
            sum += nums[i];
            if(sum<0){
                sum =0;
            }
            maxSum = max(maxSum , sum);
        }

        sum =0;
        for(int i =0;i<n;i++){
            sum+=nums[i];
            if(sum>0){
                sum =0;
            }
            minSum = min(minSum,sum);
        }

        return max(abs(minSum),abs(maxSum));
    }
};