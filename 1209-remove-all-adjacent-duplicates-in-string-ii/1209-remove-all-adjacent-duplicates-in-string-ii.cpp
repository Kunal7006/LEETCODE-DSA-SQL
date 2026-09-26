class Solution {
public:
    string removeDuplicates(string s, int k) {
        stack<pair<char,int>> st;

        for(auto &c: s){
            if(!st.empty() && st.top().first==c){
                st.top().second++;
            }else{
                st.push({c,1});
            }

            if(st.top().second == k){
                st.pop();
            }
        }

        string res = "";

        while(!st.empty()){
            char first = st.top().first;
            int second = st.top().second;
            st.pop();

            res.append(second,first);
        }

        reverse(res.begin(),res.end());
        return res;
    }
};