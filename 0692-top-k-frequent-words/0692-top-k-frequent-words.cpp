class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        int n = words.size();
        unordered_map<string,int> mp;

        for(int i=0;i<n;i++){
            mp[words[i]]++;
        }

        vector<vector<string>> bucket(n+1);

        for(auto& it:mp){
            string word = it.first;
            int freq = it.second;

            bucket[freq].push_back(word);
        } 
        for(int i = 0; i <= n; i++){
            sort(bucket[i].begin(), bucket[i].end());
        }  

        vector<string> result;

        for(int i = n; i >= 0 && k > 0; i--) {

            for(string word : bucket[i]) {
                result.push_back(word);
                k--;

                if(k == 0)
                    break;
            }
        }

        return result;
    }
};