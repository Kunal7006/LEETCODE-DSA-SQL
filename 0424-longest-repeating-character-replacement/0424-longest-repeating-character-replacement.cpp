class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int l =0;
        int r = 0;
        int maxLength = 0;
        int maxFreq = 0;
        vector<int> last(26,0);

        while(r<n){
            last[s[r]-'A']++;

            maxFreq = max(maxFreq, last[s[r]-'A']);

            while((r-l+1)-maxFreq>k){
                last[s[l]-'A']--;
                l++;
            }
            if((r-l+1)-maxFreq <=k){
                maxLength = max(maxLength,r-l+1);
            }
            r++;
        }
        return maxLength;
    }
};