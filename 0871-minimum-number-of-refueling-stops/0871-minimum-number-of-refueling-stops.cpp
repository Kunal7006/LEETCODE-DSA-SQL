class Solution {
public:
    int minRefuelStops(int target, int startFuel,
                       vector<vector<int>>& stations) {

        vector<int> v;
        v.push_back(target);
        v.push_back(0);

        stations.push_back(v);
        int n = stations.size();

        priority_queue<int> pq;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (stations[i][0] > startFuel) {
                while (startFuel < stations[i][0] && !pq.empty()) {
                    int k = pq.top();
                    startFuel += k;
                    pq.pop();
                    ans++;
                }
                if (stations[i][0] > startFuel) {
                    return -1;
                }
            }
            pq.push(stations[i][1]);
        }
        return ans;
    }
};