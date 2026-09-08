class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int m = s.length();
        int n = p.length();
        vector<int> ans;
        int sIndex = -1;

        if(n>m){
            return  ans;
        }

        vector<int> sFreq(26,0);
        vector<int> pFreq(26,0);

        for(char &ch : p){
            pFreq[ch - 'a']++;
        }

        int l =0;
        int r =0;

        while(r<m){
            sFreq[s[r]-'a']++;

            if(r-l+1 > n){
                sFreq[s[l]-'a']--;
                l++;
            }
            if(sFreq == pFreq){
                ans.push_back(l);
            }
            r++;
        }

        return ans;
    }
};