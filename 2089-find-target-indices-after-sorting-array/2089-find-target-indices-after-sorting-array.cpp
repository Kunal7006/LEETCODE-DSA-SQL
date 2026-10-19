class Solution {
public:
    int firstOccurence(vector<int>& nums, int target) {
        int n = nums.size();

        int low = 0;
        int high = n - 1;
        int ans = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                ans = mid;
                high = mid - 1;
            } else if (target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
    int lastOccurence(vector<int>& nums, int target) {
        int n = nums.size();

        int low = 0;
        int high = n - 1;
        int ans = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                ans = mid;
                low = mid + 1;
            } else if (target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int> ans;
        sort(nums.begin(), nums.end());

        int first = firstOccurence(nums, target);
        int last = lastOccurence(nums, target);
        if (first != -1) {
            for (int i = first; i <= last; i++) {
                ans.push_back(i);
            }
        }

        return ans;
    }
};