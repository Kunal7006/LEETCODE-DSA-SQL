class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();

        int sum =0;
        for(int i =0;i<n;i++){
            sum+=nums[i];
        }

        int leftSum =0;
        int rightSum = sum;

        for(int i =0;i<n;i++){
            leftSum +=nums[i];

            if(leftSum == rightSum){
                return i;
            }
            rightSum -= nums[i];
        }
        return -1;
    }
};