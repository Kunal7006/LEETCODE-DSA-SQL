class Solution {
public:
    int minChanges(string s) {
        int n = s.length();

        int i =0;
        int j =1;
        int changes =0;

        while(j<n){
            if(s[i]!=s[j]){
                changes++;
                i+=2;
                j+=2;
            }else{
                i+=2;
                j+=2;
            }
        }

        return changes;
    }
};