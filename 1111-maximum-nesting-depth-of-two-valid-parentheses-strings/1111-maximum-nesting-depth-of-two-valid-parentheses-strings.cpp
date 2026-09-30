class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int n = seq.length();
        int depth =0;
        vector<int> ans;

        for(int i =0;i<n;i++){
            if(seq[i]=='('){
                depth++;
                ans.push_back(depth % 2);
            }
            if(seq[i]==')'){
                ans.push_back(depth % 2);
                depth--;
            }
        }

        return ans;
    }
};