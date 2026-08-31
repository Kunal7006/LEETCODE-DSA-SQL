class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {

        auto critical = [](ListNode* prev, ListNode* cur, ListNode* nxt) {
            return (prev->val > cur->val && cur->val < nxt->val) ||
                   (prev->val < cur->val && cur->val > nxt->val);
        };

        ListNode* prev = head;
        ListNode* cur = head->next;
        ListNode* nxt = cur->next;

        int min_dist = INT_MAX;
        int max_dist = INT_MIN;

        int prev_crit_idx = 0;
        int first_crit_idx = 0;

        int i = 1;  // index of current node

        while (nxt != nullptr) {

            if (critical(prev, cur, nxt)) {

                if (first_crit_idx) {
                    max_dist = i - first_crit_idx;

                    min_dist = min(
                        min_dist,
                        i - prev_crit_idx
                    );
                }
                else {
                    first_crit_idx = i;
                }

                prev_crit_idx = i;
            }

            prev = cur;
            cur = nxt;
            nxt = nxt->next;

            i++;
        }

        if (min_dist == INT_MAX) {
            min_dist = -1;
            max_dist = -1;
        }

        return {min_dist, max_dist};
    }
};