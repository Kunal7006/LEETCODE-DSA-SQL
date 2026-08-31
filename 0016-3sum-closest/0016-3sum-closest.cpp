class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        int ans;
        int maxDiff = INT_MAX;
        sort(nums.begin(),nums.end());


        for (int i =0;i<n-2;i++){
            int left =i+1;
            int right = n-1;

            while(left<right){
                int sum = nums[i]+nums[left]+nums[right];
                int difference = abs(target-sum);
                if(difference<maxDiff){
                    maxDiff = difference;
                    ans = sum;
                }
                if(sum==target){
                    return sum;
                }
                if(sum<target){
                    left++;
                }
                if(sum>target){
                    right--;
                }
            }

            
        }
        return ans;

    }
};