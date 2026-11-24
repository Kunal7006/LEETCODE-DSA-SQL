class Solution {
public:
    int maxLength(vector<int>& nums) {
        int n = nums.size();
        int res = 0;

        for (int i = 0; i < n; i++) {
            long long p = 1;
            int g = 0;
            int l = 1;

            for (int j = i; j < n; j++) {
                p *= nums[j];
                g = gcd(g, nums[j]);
                l = lcm(l, nums[j]);

                if (p == l * g) {
                    res = max(res, j - i + 1);
                }

                if (p > 25200) {
                    break;
                }
            }
        }

        return res;
    }
};