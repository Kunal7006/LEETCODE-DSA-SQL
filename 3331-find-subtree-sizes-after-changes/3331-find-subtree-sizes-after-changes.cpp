class Solution {
public:
    // TC = O(n)
    unordered_map<int,vector<int>> adj;
    vector<int> resultSize;
    vector<int> last;
    void dfs(int currNode,string& s,vector<int>& parent){
        int c = s[currNode]-'a';
        int nearestAncestor = last[c];

        last[c]=currNode;
        for(int child : adj[currNode]){
            dfs(child,s,parent);
        }

        //back to currnode
        last[c]=nearestAncestor;

        
        //if currnode is root then it has no ancestor
        if(currNode!=0){
            int newParent=parent[currNode]; //old parent
            if(nearestAncestor != -1){
                newParent = nearestAncestor;
            }

            parent[currNode]=newParent;

            resultSize[newParent]+=resultSize[currNode];
        }
        

    }
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();

        //parent[i]=node -> node is the aprent of ith node
        for(int i =1;i<n;i++){
            int u = parent[i];
            int v =i;

            adj[u].push_back(v);  //u->v
        }

        resultSize.assign(n,1);
        last.assign(26,-1);

        dfs(0,s,parent);

        return resultSize;
    }
};