class Solution {
public:
    int minOperations(vector<int>& nums, int x) {

        int n = nums.size();

        int l = 0;
        int r = 0;

        int sum = 0;
        int total = 0;

        for (int num : nums) {
            total += num;
        }

        if (x > total)
            return -1;

        if (x == total)
            return n;

        int target = total - x;

        int ans = INT_MAX;

        while (r < n) {

            sum += nums[r];

            while (sum > target) {
                sum -= nums[l];
                l++;
            }

            if (sum == target) {
                ans = min(ans, l + n - 1 - r);
            }

            r++;
        }

        return ans == INT_MAX ? -1 : ans;
    }
};