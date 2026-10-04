class Solution {
public:
    vector<vector<int>> dp;

    bool solve(string &s, int n, int index, int count) {

        if(count < 0)
            return false;

        if(index == n)
            return count == 0;

        if(dp[index][count] != -1)
            return dp[index][count];

        if(s[index] == '(') {
            return dp[index][count] =
                solve(s, n, index + 1, count + 1);
        }

        if(s[index] == ')') {
            return dp[index][count] =
                solve(s, n, index + 1, count - 1);
        }

        // '*'
        return dp[index][count] =
            solve(s, n, index + 1, count + 1) ||
            solve(s, n, index + 1, count - 1) ||
            solve(s, n, index + 1, count);
    }

    bool checkValidString(string s) {
        int n = s.length();

        dp.assign(n, vector<int>(n + 1, -1));

        return solve(s, n, 0, 0);
    }
};