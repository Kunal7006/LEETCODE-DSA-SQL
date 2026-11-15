class Solution {
public:
    int MOD = 1e9 + 7;
    int numOfSubarrays(vector<int>& arr) {
        int n = arr.size();
        int oddCount = 0;
        int evenCount = 1;
        int result = 0;

        vector<int> preSum(n, 0);
        preSum[0]= arr[0];

        for (int i = 1; i < n; i++) {
            preSum[i] = preSum[i - 1] + arr[i];
        }

        for (int i = 0; i < n; i++) {
            if (preSum[i] % 2 == 0) {
                result = (result + oddCount) % MOD;
                evenCount++;
            } else {
                result = (result + evenCount) % MOD;
                oddCount++;
            }
        }

        return result;
    }
};