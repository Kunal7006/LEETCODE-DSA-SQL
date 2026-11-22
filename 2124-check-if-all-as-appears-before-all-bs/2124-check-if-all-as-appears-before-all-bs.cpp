class Solution {
public:
    bool checkString(string s) {
        int n = s.length();

        int i =0;
        int j =1;
        while(j<n){
            if(s[i]=='b' && s[j]=='a'){
                return false;
            }else{
                i++;
                j++;
            }
        }
        return true;
    }
};