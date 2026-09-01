class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        int left =0;
        int right = n-1;

       while(left < n - 1) {
            if(nums[left] > nums[left + 1]) {
                break;
            }
            left++;
        }
        if(left==n-1){
            return 0;
        }
        while(right > 0) {
            if(nums[right - 1] > nums[right]) {
                break;
            }
            right--;
        }

        int maximum =INT_MIN;
        int minimum = INT_MAX;

        for(int i=left;i<=right;i++){
            if(nums[i]>maximum){
                maximum = nums[i];
            }
            if(nums[i]<minimum){
                minimum = nums[i];
            }
        }

        while(left>0 && nums[left-1]>minimum){
            left--;
        }
        while(right<n-1 && nums[right+1]<maximum){
            right++;
        }
        int ans = right - left+1;
        return ans;

    }
};