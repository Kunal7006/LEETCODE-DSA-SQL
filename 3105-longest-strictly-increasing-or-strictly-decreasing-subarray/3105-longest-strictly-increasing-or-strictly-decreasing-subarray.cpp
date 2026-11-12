class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();

        int i =0;
        int j =1;
        int maxLength =1;

        while(j<n){
            if(nums[j]>nums[j-1]){
                maxLength=max(maxLength,j-i+1);
                j++;
                
            }else{
                i=j;
                j=i+1;
            }
        }

        i=0;
        j=1;
        while(j<n){
            if(nums[j]<nums[j-1]){
                maxLength=max(maxLength,j-i+1);
                j++;
                
            }
            else{
                i=j;
                j=i+1;
            }
        }

        return maxLength;
    }
};