class Solution {
public:
    string minWindow(string s, string t) {

        vector<int> freq(256, 0);

        int m = s.length();
        int n = t.length();

        int minLength = INT_MAX;
        int count = 0;
        int sIndex = -1;

        // Frequency of characters required from t
        for (int i = 0; i < n; i++) {
            freq[t[i]]++;
        }

        int l = 0;
        int r = 0;

        while (r < m) {

            // Add s[r] to window
            if (freq[s[r]] > 0) {
                count++;
            }

            freq[s[r]]--;

            // Window is valid
            while (count == n) {

                // Update minimum window
                if (r - l + 1 < minLength) {
                    minLength = r - l + 1;
                    sIndex = l;
                }

                // Remove s[l] from window
                freq[s[l]]++;

                // If frequency becomes positive,
                // we just removed a required character
                if (freq[s[l]] > 0) {
                    count--;
                }

                l++;
            }

            r++;
        }

        if (sIndex == -1) {
            return "";
        }

        return s.substr(sIndex, minLength);
    }
};