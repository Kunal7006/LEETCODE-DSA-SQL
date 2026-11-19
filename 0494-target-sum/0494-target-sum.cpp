class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int S = accumulate(nums.begin(),nums.end(),0);

        vector<vector<int>> t(n+1,vector<int>(2*S+1,0));
        // Base case: 0 elements, sum = 0
        t[0][S] = 1;

        for(int i = 1; i <= n; i++) {
            for(int j = -S; j <= S; j++) {

                // If previous sum is reachable
                if(t[i-1][j+S] != 0) {

                    // Plus choice
                    if(j + nums[i-1] <= S) {
                        t[i][j + nums[i-1] + S] += t[i-1][j+S];
                    }

                    // Minus choice
                    if(j - nums[i-1] >= -S) {
                        t[i][j - nums[i-1] + S] += t[i-1][j+S];
                    }
                }
            }
        }

        if(target < -S || target > S) {
            return 0;
        }

        return t[n][target + S];
    }
};