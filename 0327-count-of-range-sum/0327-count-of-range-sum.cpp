class Solution {
public:

    long long mergeSort(vector<long long>& prefix, int left, int right,
                        long long lower, long long upper) {

        // Base case
        if (left >= right)
            return 0;

        int mid = left + (right - left) / 2;

        // Count valid pairs in left half
        long long count = mergeSort(prefix, left, mid, lower, upper);

        // Count valid pairs in right half
        count += mergeSort(prefix, mid + 1, right, lower, upper);

        // Count valid pairs where
        // i is in left half and j is in right half
        int lo = mid + 1;
        int hi = mid + 1;

        for (int i = left; i <= mid; i++) {

            // Find first prefix[j] >= prefix[i] + lower
            while (lo <= right &&
                   prefix[lo] - prefix[i] < lower) {
                lo++;
            }

            // Find first prefix[j] > prefix[i] + upper
            while (hi <= right &&
                   prefix[hi] - prefix[i] <= upper) {
                hi++;
            }

            // All elements between lo and hi-1 are valid
            count += hi - lo;
        }

        // Merge the two sorted halves
        vector<long long> temp;
        int i = left;
        int j = mid + 1;

        while (i <= mid && j <= right) {

            if (prefix[i] <= prefix[j]) {
                temp.push_back(prefix[i]);
                i++;
            }
            else {
                temp.push_back(prefix[j]);
                j++;
            }
        }

        while (i <= mid) {
            temp.push_back(prefix[i]);
            i++;
        }

        while (j <= right) {
            temp.push_back(prefix[j]);
            j++;
        }

        // Copy back
        for (int k = 0; k < temp.size(); k++) {
            prefix[left + k] = temp[k];
        }

        return count;
    }


    long long countRangeSum(vector<int>& nums, int lower, int upper) {

        int n = nums.size();

        // Prefix sum
        vector<long long> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        // Count valid prefix-sum pairs
        return mergeSort(prefix, 0, n, lower, upper);
    }
};