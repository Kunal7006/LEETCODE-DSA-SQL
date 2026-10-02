class Solution {
public:
    int allocatePainters(vector<int>& nums, int mid){
        int painters = 1;
        int wallPainters=0;
        for(int i =0;i<nums.size();i++){
            if(wallPainters + nums[i]<=mid){
                wallPainters += nums[i];
            }else{
                painters++;
                wallPainters = nums[i];
            }
        }
        return painters;
    }
    int splitArray(vector<int>& nums, int k) {
        int low = *max_element(nums.begin(),nums.end());
        int high = accumulate(nums.begin(),nums.end(),0);

        while(low<=high){
            int mid = low +(high - low)/2;

            int painters = allocatePainters(nums,mid);

            if(painters > k){
                low = mid +1;
            }
            else{
                high = mid -1;
            }
        }
        return low;
    }
};