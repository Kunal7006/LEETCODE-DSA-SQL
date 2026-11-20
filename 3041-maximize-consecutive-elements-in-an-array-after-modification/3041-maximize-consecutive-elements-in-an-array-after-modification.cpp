class Solution {
public:
    int n;
    vector<vector<int>> dp;
    int findMethod(vector<int>& nums,int start,int target){
        int j = lower_bound(nums.begin()+start,nums.end(),target)-nums.begin();

        if(j<n && nums[j]==target){
            return j;
        }
        return -1;
    }
    // int solve(int i,int inc,vector<int>& nums){

    //     if(memo[i][inc]!=-1){
    //         return memo[i][inc];
    //     }
    //     int currVal = nums[i]+inc; //inc->0/1

    //     int len = 1;
    //     //1st optiom->find currVal+1
    //     int j = findMethod(nums,i+1,currVal+1);
    //     if(j!=-1){
    //         len=max(len,1+solve(j,0,nums));
    //     }
    //     //2nd optiom->find currVal and then increment by +1
    //     j = findMethod(nums,i+1,currVal);
    //     if(j!=-1){
    //         len=max(len,1+solve(j,1,nums));
    //     }
    //     return memo[i][inc]=len;
    // }
    int maxSelectedElements(vector<int>& nums) {
        n = nums.size();

        sort(nums.begin(),nums.end());
        dp.assign(n+1,vector<int>(2,0));
        int result =1;

        for(int i =n-1;i>=0;i--){
            for(int inc =0;inc<2;inc++){
                int currVal = nums[i]+inc;
                int len =1;

                //1st option
                int j = findMethod(nums,i+1,currVal+1);
                if(j!=-1){
                    len=max(len,1+dp[j][0]);
                }

                //2nd option
                j = findMethod(nums,i+1,currVal);
                if(j!=-1){
                    len=max(len,1+dp[j][1]);
                }
            

                dp[i][inc]=len;
                result = max(result,len);
            }
        }
    
        return result;
    }
};