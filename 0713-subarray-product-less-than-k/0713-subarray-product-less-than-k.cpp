class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1)
            return 0;

        int left = 0;
        int product = 1;
        int count = 0;

        for (int right = 0; right < nums.size(); right++) {

            product *= nums[right];

            // Shrink window until product < k
            while (product >= k) {
                product /= nums[left];
                left++;
            }

            // Number of valid subarrays ending at right
            count += right - left + 1;
        }

        return count;
    }
};