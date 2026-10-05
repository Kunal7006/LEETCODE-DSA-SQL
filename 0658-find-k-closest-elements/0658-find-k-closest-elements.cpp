class Solution {
public:
    typedef pair<int,int> P;
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();

        priority_queue<P> pq;

        for(int& num:arr){
            int distance = abs(num-x);

            pq.push({distance,num});

            if(pq.size()>k){
                pq.pop();
            }
        }

        vector<int> result;

        while(!pq.empty()){
            result.push_back(pq.top().second);
            pq.pop();
        }
        sort(result.begin(),result.end());
        return result;
    }
};