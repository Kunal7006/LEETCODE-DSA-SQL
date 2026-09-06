class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        vector<int> hash(256,-1);

        int maxLength =0;
        int l=0;
        int r =0;

        while(r<n){
            if(hash[s[r]]!=-1){
                if(hash[s[r]]>=l){
                    l = hash[s[r]]+1;
                }
            }

            hash[s[r]]=r;
            maxLength = max(maxLength,r-l+1);
            r++;
        }
        return maxLength;
    }
};