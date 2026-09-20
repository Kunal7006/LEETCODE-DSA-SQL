class Solution {
public:
    int reverseDegree(string s) {
        int n = s.length();

        int rDegree = 0;

        for(int i=1;i<=n;i++){
            int product = (26-(s[i-1]-'a')) * i ;

            rDegree += product;
        }
        return rDegree;
        
    }
};