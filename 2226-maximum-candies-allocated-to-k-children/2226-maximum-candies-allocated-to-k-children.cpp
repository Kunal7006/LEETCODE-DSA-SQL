class Solution {
public:
    bool canGiveCandies(vector<int>& candies,int mid,long long k){
        int n = candies.size();
        long long  childCount =0;

        for(int i =0;i<n;i++){
           childCount+= candies[i]/mid;

           if(childCount>=k){
            return true;
           }
        }
        return false;
    }

    int maximumCandies(vector<int>& candies, long long k) {
        int n = candies.size();
        int low = 1;
        int high = *max_element(candies.begin(),candies.end());
        

        while(low <= high){
            int mid = low+(high-low)/2;
            if(canGiveCandies(candies,mid,k)){
                low = mid +1;
            }
            else{
                high = mid-1;
            }
        }
        return high;
    }
};