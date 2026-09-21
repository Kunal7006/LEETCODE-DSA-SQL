class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> result(k, 0);
        vector<long long> prevRemainderCount(k, 0);

        for (int i = 0; i < n; i++) {
            vector<long long> currentRemainderCount(k, 0);

            int numRemainder = nums[i] % k;
            currentRemainderCount[numRemainder]++;

            for (int oldRemainder = 0; oldRemainder < k; oldRemainder++) {
                int newRemainder = (oldRemainder * numRemainder) % k;

                currentRemainderCount[newRemainder] +=
                    prevRemainderCount[oldRemainder];
            }

            prevRemainderCount = currentRemainderCount;

            for (int remainder = 0; remainder < k; remainder++) {
                result[remainder] += prevRemainderCount[remainder];
            }
        }
        return result;
    }
};