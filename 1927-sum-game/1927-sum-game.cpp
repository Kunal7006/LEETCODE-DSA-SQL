class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();

        int leftSum = 0;
        int rightSum = 0;

        int leftQ = 0;
        int rightQ = 0;

        for (int i = 0; i < n / 2; i++) {
            if (num[i] == '?') {
                leftQ++;
            } else {
                leftSum += num[i] - '0';
            }
        }

        for (int i = n / 2; i < n; i++) {
            if (num[i] == '?') {
                rightQ++;
            } else {
                rightSum += num[i] - '0';
            }
        }

        // If odd number of question marks,
        // Alice gets an extra move and wins.
        if ((leftQ + rightQ) % 2 == 1) {
            return true;
        }

        // Bob wins only if this expression becomes 0.
        return 2 * (leftSum - rightSum)
                + 9 * (leftQ - rightQ) != 0;
    }
};