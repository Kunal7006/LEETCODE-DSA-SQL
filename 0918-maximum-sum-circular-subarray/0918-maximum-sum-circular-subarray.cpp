class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        int totalSum =0;

        for(int i=0;i<n;i++){
            totalSum+=nums[i];
        }
        int minSum = INT_MAX;
        
        int sum =0;
        for(int i=0;i<n;i++){
            sum += nums[i];

            minSum = min(minSum, sum);
            if(sum>0){
                sum =0;
            }
            

        }
        sum =0;
        int maxSum =INT_MIN;
        for(int i=0;i<n;i++){
            sum += nums[i];
            maxSum = max(maxSum, sum);
            if(sum<0){
                sum =0;
            }
        

        }

        // corner case for all negative 
        if(maxSum<0){
            return maxSum;
        }



        return max(maxSum,totalSum - minSum);

    }
};