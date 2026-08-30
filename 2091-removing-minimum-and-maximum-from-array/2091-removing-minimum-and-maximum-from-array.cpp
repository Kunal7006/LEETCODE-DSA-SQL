class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        if (n == 1) {
            return 1;
        }

        int minIndex = 0;
        int maxIndex = 0;

        // Find indices of minimum and maximum
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }

            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }

        // Put smaller index in left
        // and larger index in right
        int left = min(minIndex, maxIndex);
        int right = max(minIndex, maxIndex);

        // 1. Remove both from the front
        int fromFront = right + 1;

        // 2. Remove both from the back
        int fromBack = n - left;

        // 3. Remove left from front and right from back
        int fromBoth = (left + 1) + (n - right);

        return min({fromFront, fromBack, fromBoth});
    }
};