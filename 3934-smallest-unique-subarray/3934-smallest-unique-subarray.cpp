class Solution {
public:
    typedef long long ll;

    const ll base = 100003;
    const ll mod1 = 1000000007;
    const ll mod2 = 1000000009;

    bool check(vector<int>& nums, int k) {
        int n = nums.size();

        unordered_map<ll, int> mp;

        ll h1 = 0, h2 = 0;
        ll p1 = 1, p2 = 1;

        // Calculate base^(k-1)
        for (int i = 0; i < k - 1; i++) {
            p1 = (p1 * base) % mod1;
            p2 = (p2 * base) % mod2;
        }

        // Calculate hash of first window
        for (int i = 0; i < k; i++) {
            h1 = (h1 * base + nums[i]) % mod1;
            h2 = (h2 * base + nums[i]) % mod2;
        }

        mp[h1 * mod2 + h2]++;

        // Rolling hash
        for (int i = k; i < n; i++) {

            // Remove outgoing element
            h1 = (h1 - nums[i-k] * p1 % mod1 + mod1) % mod1;
            h2 = (h2 - nums[i-k] * p2 % mod2 + mod2) % mod2;

            // Add incoming element
            h1 = (h1 * base + nums[i]) % mod1;
            h2 = (h2 * base + nums[i]) % mod2;

            mp[h1 * mod2 + h2]++;
        }

        // Check if any subarray occurs exactly once
        for (auto& it : mp) {
            if (it.second == 1) {
                return true;
            }
        }

        return false;
    }

    int smallestUniqueSubarray(vector<int>& nums) {
        int low = 1;
        int high = nums.size();
        int ans = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (check(nums, mid)) {
                ans = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }

        return ans;
    }
};