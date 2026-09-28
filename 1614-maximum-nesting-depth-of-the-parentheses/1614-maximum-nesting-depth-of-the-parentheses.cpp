class Solution {
public:
    int maxDepth(string s) {
        int n = s.length();
        int count =0;
        int maxDepth =0;

        for(int i=0;i<n;i++){
            if(s[i]=='('){
                count++;
                maxDepth =max(maxDepth,count);
            }else if(s[i]==')'){
                count--;
            }else{
                continue;
            }
        }
        return maxDepth;
        
    }
};