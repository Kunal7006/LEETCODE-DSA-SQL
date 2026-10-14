class Solution {
public:
    int n;
    bool isPalindrome(string s,int low,int high){
        while(low<high){
            if(s[low]!=s[high]){
                return false;
            }
            low++;
            high--;
        }
        return true;
    }
    void backtrack(int index,string s,vector<vector<string>>& result,vector<string> curr){
        if(index==n){
            result.push_back(curr);
            return;
        }

        for(int i =index;i<n;i++){
            if(isPalindrome(s,index,i)){
                curr.push_back(s.substr(index,i-index+1));
                backtrack(i+1,s,result,curr);
                curr.pop_back();
            }
        }

    }
    vector<vector<string>> partition(string s) {
        n = s.length();
        vector<vector<string>> result;
        vector<string> curr;

        backtrack(0,s,result,curr);
        return result;
    }
};