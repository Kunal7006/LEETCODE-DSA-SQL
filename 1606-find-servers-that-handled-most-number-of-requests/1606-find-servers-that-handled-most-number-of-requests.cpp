class Solution {
public:
    // TC = n log k
    typedef pair<int,int> P; // finishtime,server ids
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        set<int> available_servers;
        for(int i =0;i<k;i++){
            available_servers.insert(i);
        }

        priority_queue<P,vector<P>,greater<P>> busyServers;

        vector<int> countRequest(k,0);

        for(int i =0;i<arrival.size();i++){
            int time = arrival[i];

            while(!busyServers.empty() && busyServers.top().first <= time){
                int server = busyServers.top().second;

                busyServers.pop();

                available_servers.insert(server);
            }

            int target = i%k;
            auto it = available_servers.lower_bound(target);

            if(it == available_servers.end()){ // wrap around
                it = available_servers.begin();
            }

            if(available_servers.empty()){
                continue; // no servers available 
            }
            int targetServer = *it;

            available_servers.erase(it); // this server is going to be busy 

            busyServers.push({time+load[i],targetServer});

            countRequest[targetServer]++;
        }

        int maxNumberOfRequests = * max_element(countRequest.begin(),countRequest.end());

        vector<int> result;

        for(int i =0;i<k;i++){
            if(countRequest[i]==maxNumberOfRequests){
                result.push_back(i);
            }
        }

        return result;
    }
};