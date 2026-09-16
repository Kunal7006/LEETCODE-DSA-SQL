class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        int n = firstList.size();
        int m = secondList.size();
        vector<vector<int>> ans;

        int first =0;
        int second =0;

        while(first<n && second<m){
            if(firstList[first][1]>=secondList[second][0] && firstList[first][0]<= secondList[second][1]){
                vector<int> temp(2);
                temp[0]= max(firstList[first][0],secondList[second][0]);
                temp[1]= min(firstList[first][1],secondList[second][1]);
                ans.push_back(temp);
            }
            if(firstList[first][1]<secondList[second][1]){
                first++;
            }
            else{
                second++;
            }
        }
        return ans;
    }
};