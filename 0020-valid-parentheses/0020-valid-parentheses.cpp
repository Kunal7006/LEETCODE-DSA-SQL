class Solution {
public:
    bool isValid(string s) {
        int n = s.length();
        stack<char> st;

        for(int i =0;i<n;i++){
            char ch = s[i];
            if(s[i]=='(' || s[i]=='{' || s[i]== '['){
                st.push(ch);
            }else if(!st.empty()){
                if(st.top()=='(' && s[i]==')' || st.top()=='{' && s[i]=='}' || st.top()=='[' and s[i]==']'){
                    st.pop();
                }
                else{
                    return false;
                }
            }else{
                return false;
            }
        }
        if(st.empty()){
            return true;
        }else{
            return false;
        }

    }
};