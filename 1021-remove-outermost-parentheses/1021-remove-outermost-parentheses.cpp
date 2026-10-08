class Solution {
public:
    string removeOuterParentheses(string s) {
       stack<char>stack;
        string ans;
        if(s.empty())return "";
        int n=s.length();
        for(int i=0;i<n;i++){
            if(stack.empty()) {
                stack.push(s[i]);
                continue;
            }
            if(s[i]=='('){
                stack.push('(');
            }
            if(s[i]==')'){
                stack.pop();
            }
            if(!stack.empty()) {
                
                ans+=s[i];
            }

        }
        return ans;
        
    }
};