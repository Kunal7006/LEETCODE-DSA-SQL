class Solution {
public:
    static const int MOD = 1e9 + 7;

    struct Node {
        long long sum = 0;
        long long sq = 0;
        long long lazy = 0;
    };

    vector<Node> seg;
    int n;

    void apply(int idx, int l, int r, long long val) {
        long long len = r - l + 1;
        long long oldSum = seg[idx].sum;

        seg[idx].sq = (seg[idx].sq
            + 2LL * val * oldSum
            + val * val % MOD * len) % MOD;

        seg[idx].sum = (oldSum + val * len) % MOD;
        seg[idx].lazy = (seg[idx].lazy + val) % MOD;
    }

    void push(int idx, int l, int r) {
        if (seg[idx].lazy == 0 || l == r) return;

        int mid = (l + r) / 2;
        long long val = seg[idx].lazy;

        apply(2 * idx, l, mid, val);
        apply(2 * idx + 1, mid + 1, r, val);

        seg[idx].lazy = 0;
    }

    void update(int idx, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return;

        if (ql <= l && r <= qr) {
            apply(idx, l, r, 1);
            return;
        }

        push(idx, l, r);

        int mid = (l + r) / 2;

        update(2 * idx, l, mid, ql, qr);
        update(2 * idx + 1, mid + 1, r, ql, qr);

        seg[idx].sum = (seg[2 * idx].sum
                      + seg[2 * idx + 1].sum) % MOD;

        seg[idx].sq = (seg[2 * idx].sq
                     + seg[2 * idx + 1].sq) % MOD;
    }

    int sumCounts(vector<int>& nums) {
        n = nums.size();
        seg.assign(4 * n, Node());

        unordered_map<int, int> last;
        long long ans = 0;

        for (int i = 0; i < n; i++) {
            int prev = -1;

            if (last.count(nums[i])) {
                prev = last[nums[i]];
            }

            update(1, 0, n - 1, prev + 1, i);

            ans = (ans + seg[1].sq) % MOD;

            last[nums[i]] = i;
        }

        return ans;
    }
};