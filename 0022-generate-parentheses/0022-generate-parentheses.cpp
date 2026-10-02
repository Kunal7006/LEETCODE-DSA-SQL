class Solution {
    private:
    void solve(vector<string>& ans,int oc,int cc,int n , string temp){
        if(oc==n && cc==n){
            ans.push_back(temp);
            return;
        }
        if(oc<n){
            solve(ans,oc+1,cc,n,temp+"(");

        }
        if(cc<oc){
             solve(ans,oc,cc+1,n,temp+")");
        }
    }
public:
    vector<string> generateParenthesis(int n) {

        vector<string> ans;
        int oc=0,cc=0;
        solve(ans,oc,cc,n,"");
        return ans;
        
    }
};