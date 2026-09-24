class Solution {
public:
    int digitSum(int n){
        int sum =0;
        while(n){
            int digit = n % 10;
            sum +=digit;
            n = n/10;
        }
        return sum;
    }
    int smallestIndex(vector<int>& nums) {
        
        int n = nums.size();
        int ans =-1;

        for(int i =0;i<n;i++){
            if(digitSum(nums[i])==i){
                ans = i;
                break;
            }
        }
        return ans;
    }
};