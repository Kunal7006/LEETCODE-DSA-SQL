class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int n = nums1.size();
        int minimum = INT_MAX;
        bool allEven = true;

        for (int i=0;i<n;i++){
            minimum = min(minimum,nums1[i]);

            if(nums1[i]%2 !=0){
                allEven = false;
            }
        }

        if(minimum%2 !=0){
            return true;
        }
        if(allEven){
            return true;
        }
        return false;
    }
};