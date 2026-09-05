class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        map<int,int> mp;
        int l=0;
        int r=0;
        int maxFruits = 0;

        while(r<n){
            mp[fruits[r]]++;
            
            if(mp.size()>2){
                mp[fruits[l]]--;
                if(mp[fruits[l]]==0){
                    mp.erase(fruits[l]);
                }
                l++;
            }


            maxFruits = max(maxFruits,r-l+1);
            r++;
        }

        return maxFruits;
    }
};