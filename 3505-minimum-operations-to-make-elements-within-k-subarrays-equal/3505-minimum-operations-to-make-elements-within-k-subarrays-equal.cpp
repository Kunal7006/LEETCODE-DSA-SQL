class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size();

        // Step 1: Calculate the cost of every window of size x
        multiset<int> left, right;
        long long sumLeft = 0, sumRight = 0;

        auto balance = [&]() {
            int total = left.size() + right.size();
            int target = (total + 1) / 2;

            while ((int)left.size() > target) {
                int val = *left.rbegin();
                left.erase(prev(left.end()));
                sumLeft -= val;

                right.insert(val);
                sumRight += val;
            }

            while ((int)left.size() < target) {
                int val = *right.begin();
                right.erase(right.begin());
                sumRight -= val;

                left.insert(val);
                sumLeft += val;
            }
        };

        auto add = [&](int val) {
            if (left.empty() || val <= *left.rbegin()) {
                left.insert(val);
                sumLeft += val;
            } else {
                right.insert(val);
                sumRight += val;
            }
            balance();
        };

        auto remove = [&](int val) {
            auto it = left.find(val);

            if (it != left.end()) {
                left.erase(it);
                sumLeft -= val;
            } else {
                it = right.find(val);
                right.erase(it);
                sumRight -= val;
            }
            balance();
        };

        auto getCost = [&]() -> long long {
            long long med = *left.rbegin();

            return med * left.size() - sumLeft
                 + sumRight - med * right.size();
        };

        vector<long long> cost(n - x + 1);

        for (int i = 0; i < n; i++) {
            add(nums[i]);

            if (i >= x - 1) {
                cost[i - x + 1] = getCost();
                remove(nums[i - x + 1]);
            }
        }

        // Step 2: DP to choose k non-overlapping windows
        const long long INF = LLONG_MAX / 4;

        vector<long long> prevDP(n + 1, 0);
        vector<long long> currDP(n + 1);

        for (int j = 1; j <= k; j++) {
            fill(currDP.begin(), currDP.end(), INF);

            for (int i = x; i <= n; i++) {

                // Choice 1: Skip current element
                currDP[i] = currDP[i - 1];

                // Choice 2: Take window ending at i-1
                if (prevDP[i - x] != INF) {
                    currDP[i] = min(
                        currDP[i],
                        prevDP[i - x] + cost[i - x]
                    );
                }
            }

            prevDP.swap(currDP);
        }

        return prevDP[n];
    }
};