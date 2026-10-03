class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
        int open = 0;
        int close = 0;
        int ans = 0;

        //left to right traversal 
        for (int i = 0; i < n; i++) {
            if(s[i]=='('){
                open++;
            }
            if(s[i]==')'){
                close++;
            }
            if(close>open){
                open =0;
                close=0;
            }
            if(open == close){
                ans = max(ans,open+close);
            }
            
        }

        // check right to left traversal also 
        open =0;
        close =0;

        for(int i= n-1;i>=0;i--){
            if(s[i]=='('){
                open++;
            }
            if(s[i]==')'){
                close++;
            }
            if(open>close){
                open =0;
                close =0;
            }
            if(open == close){
                ans = max(ans,open +close);
            }
            
        }

        return ans;
    }
};