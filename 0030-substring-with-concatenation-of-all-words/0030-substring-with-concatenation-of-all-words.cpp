class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {

        vector<int> ans;

        int m = s.length();
        int wordLen = words[0].length();
        int wordCount = words.size();

        int totalLen = wordLen * wordCount;

        if (totalLen > m)
            return ans;

        unordered_map<string, int> required;

        for (string word : words) {
            required[word]++;
        }

        // We need wordLen different starting offsets
        for (int offset = 0; offset < wordLen; offset++) {

            int l = offset;
            int r = offset;

            unordered_map<string, int> current;
            int count = 0;

            while (r + wordLen <= m) {

                // Take one word from s
                string word = s.substr(r, wordLen);
                r += wordLen;

                // Word is not required
                if (required.find(word) == required.end()) {

                    current.clear();
                    count = 0;
                    l = r;
                }
                else {

                    current[word]++;
                    count++;

                    // Too many occurrences of this word
                    while (current[word] > required[word]) {

                        string leftWord = s.substr(l, wordLen);

                        current[leftWord]--;
                        count--;

                        l += wordLen;
                    }

                    // We have exactly all required words
                    if (count == wordCount) {

                        ans.push_back(l);

                        // Move left to look for next window
                        string leftWord = s.substr(l, wordLen);

                        current[leftWord]--;
                        count--;

                        l += wordLen;
                    }
                }
            }
        }

        return ans;
    }
};