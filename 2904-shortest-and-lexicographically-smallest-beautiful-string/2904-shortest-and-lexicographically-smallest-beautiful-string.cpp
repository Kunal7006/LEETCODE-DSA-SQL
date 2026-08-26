class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        vector<int> ones;

        // Store positions of all '1's
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1') {
                ones.push_back(i);
            }
        }

        // Not enough 1s
        if (ones.size() < k) {
            return "";
        }

        int minLen = INT_MAX;
        string answer = "";

        // Check every group of k consecutive 1s
        for (int i = 0; i <= ones.size() - k; i++) {
            int start = ones[i];
            int end = ones[i + k - 1];

            string substring = s.substr(start, end - start + 1);
            int length = substring.size();

            if (length < minLen) {
                minLen = length;
                answer = substring;
            }
            else if (length == minLen && substring < answer) {
                answer = substring;
            }
        }

        return answer;
    }
};