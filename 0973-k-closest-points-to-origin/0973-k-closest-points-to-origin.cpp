class Solution {
public:
    typedef pair<int, vector<int>> P;

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        // Max heap
        priority_queue<P> pq;

        for(auto& point : points) {

            int x = point[0];
            int y = point[1];

            // No need for sqrt
            int distance = x * x + y * y;

            pq.push({distance, point});

            if(pq.size() > k) {
                pq.pop();
            }
        }

        vector<vector<int>> result;

        while(!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};