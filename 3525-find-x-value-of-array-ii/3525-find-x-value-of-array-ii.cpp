class Solution {
public:

    struct Node {
        int prod;
        vector<long long> pref;

        Node() {
            prod = 0;
        }

        Node(int k) {
            prod = 1 % k;
            pref.assign(k, 0);
        }
    };

    int n, k;
    vector<Node> seg;

    // Merge two nodes
    Node mergeNode(const Node& left, const Node& right) {

        Node res(k);

        // Product of complete combined segment
        res.prod = (left.prod * right.prod) % k;

        // Prefixes completely inside left
        for (int r = 0; r < k; r++) {
            res.pref[r] += left.pref[r];
        }

        // Prefixes that contain all of left
        // and then some prefix of right
        for (int r = 0; r < k; r++) {

            int newRemainder =
                (left.prod * r) % k;

            res.pref[newRemainder] += right.pref[r];
        }

        return res;
    }

    // Build segment tree
    void build(vector<int>& nums, int node, int l, int r) {

        if (l == r) {

            // IMPORTANT:
            // Initialize pref vector before accessing it
            seg[node] = Node(k);

            int rem = nums[l] % k;

            seg[node].prod = rem;
            seg[node].pref[rem] = 1;

            return;
        }

        int mid = (l + r) / 2;

        build(nums, node * 2, l, mid);

        build(nums, node * 2 + 1, mid + 1, r);

        seg[node] = mergeNode(
            seg[node * 2],
            seg[node * 2 + 1]
        );
    }

    // Point update
    void update(
        int node,
        int l,
        int r,
        int idx,
        int value
    ) {

        if (l == r) {

            // IMPORTANT:
            // Reinitialize the node
            seg[node] = Node(k);

            int rem = value % k;

            seg[node].prod = rem;
            seg[node].pref[rem] = 1;

            return;
        }

        int mid = (l + r) / 2;

        if (idx <= mid) {

            update(
                node * 2,
                l,
                mid,
                idx,
                value
            );

        } else {

            update(
                node * 2 + 1,
                mid + 1,
                r,
                idx,
                value
            );
        }

        // Recalculate parent
        seg[node] = mergeNode(
            seg[node * 2],
            seg[node * 2 + 1]
        );
    }

    // Range query
    Node query(
        int node,
        int l,
        int r,
        int ql,
        int qr
    ) {

        // Completely inside
        if (ql <= l && r <= qr) {
            return seg[node];
        }

        int mid = (l + r) / 2;

        // Completely in left
        if (qr <= mid) {

            return query(
                node * 2,
                l,
                mid,
                ql,
                qr
            );
        }

        // Completely in right
        if (ql > mid) {

            return query(
                node * 2 + 1,
                mid + 1,
                r,
                ql,
                qr
            );
        }

        // Overlapping both sides
        Node leftPart = query(
            node * 2,
            l,
            mid,
            ql,
            qr
        );

        Node rightPart = query(
            node * 2 + 1,
            mid + 1,
            r,
            ql,
            qr
        );

        return mergeNode(leftPart, rightPart);
    }

    vector<int> resultArray(
        vector<int>& nums,
        int k,
        vector<vector<int>>& queries
    ) {

        this->k = k;
        this->n = nums.size();

        // Allocate segment tree
        seg.resize(4 * n + 5);

        // Build
        build(
            nums,
            1,
            0,
            n - 1
        );

        vector<int> answer;

        for (auto& q : queries) {

            int index = q[0];
            int value = q[1];
            int start = q[2];
            int x = q[3];

            // Update nums[index] = value
            update(
                1,
                0,
                n - 1,
                index,
                value
            );

            // Query [start, n - 1]
            Node res = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            );

            // Number of prefixes having
            // product % k == x
            answer.push_back(
                (int)res.pref[x]
            );
        }

        return answer;
    }
};