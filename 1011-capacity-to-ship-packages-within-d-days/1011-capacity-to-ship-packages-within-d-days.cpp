class Solution {
public:
    int canShip(vector<int>& weights,int mid){
        int days =1;
        int load = 0;

        for(int i =0;i<weights.size();i++){
            if(load+weights[i]>mid){
                days++;
                load = weights[i];
            }
            else{
                load+=weights[i];
            }
        }
        return days;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int low = *max_element(weights.begin(),weights.end());
        int high = accumulate(weights.begin(),weights.end(),0);

        while(low<=high){
            int mid = low +(high -low)/2;

            if(canShip(weights,mid)<=days){
                high = mid-1;
            }
            else{
                low = mid +1;
            }
        }
        return low;
    }
};