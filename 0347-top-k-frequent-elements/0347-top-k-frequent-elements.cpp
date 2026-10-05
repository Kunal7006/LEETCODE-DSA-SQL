class Solution {
public:
    typedef pair<int,int> P;
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;

        for(int &num: nums){
            mp[num]++;
        }

        // define min heap
        priority_queue<P,vector<P>,greater<P>> pq;

        //push elements in min heap
        //maintain size of k only 

        for(auto& it:mp){
            int value = it.first;
            int freq = it.second;
            
            pq.push({freq,value});
            
            if(pq.size()>k){
                pq.pop();
            }        
        }

        vector<int> result;
        while(!pq.empty()){
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};