class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();

        vector<int> sorted; // empty in the beginning

        for(int i =0;i<n;i++){
            auto it = lower_bound(sorted.begin(),sorted.end(),nums[i]); // just greater than or equal to

            if(it == sorted.end()){
                sorted.push_back(nums[i]); // greatest : so insert it 
            }else{
                *it = nums[i]; // replace with nums[i]
            }

        }
        return sorted.size();
    }
};