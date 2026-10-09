class Solution {
public:
    int minInsertions(string s) {
        int ans = 0;
        int open = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                open++;
            }
            else {
                // Check if the next character is also ')'
                if (i + 1 < s.size() && s[i + 1] == ')') {
                    i++;
                }
                else {
       
                    // Insert one ')' to make a pair
                    ans++;
                }

                if (open > 0) {
                    open--;
                }
                else {
                    // Insert '(' to match the closing pair
                    ans++;
                }
            }
        }

        // Every remaining '(' needs two ')'
        ans += open * 2;

        return ans;
    }
};