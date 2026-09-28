class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> mp1;
        unordered_map<char,int> mp2;

        for(auto& ch : ransomNote){
            mp1[ch]++;
        }
        for(auto& ch : magazine){
            mp2[ch]++;
        }
        bool ans = true;
        for(auto& it : mp1){
            if(it.second > mp2[it.first]){
                ans = false;
                break;
            }
        }
        return ans;
    }
};