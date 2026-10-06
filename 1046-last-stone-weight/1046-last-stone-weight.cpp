class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        

        while(stones.size()>1){
            sort(stones.begin(),stones.end());

            int a = stones.back();
            stones.pop_back();
            int b = stones.back();
            stones.pop_back();

            if(abs(a-b)!=0){
                stones.push_back(abs(a-b));
            }
        }
        if(stones.empty())
            return 0;

        return stones[0];
    }
};