class Solution {
    private:
    int firstOccurrence(vector<int>& nums,int target){
        int n = nums.size();
        int s=0;
        int e=n-1;

        int ans=-1;

        while(s<=e){
            int mid=s+(e-s)/2;
            if(nums[mid]==target){
                ans=mid;
                e=mid-1;
            }
            else if(nums[mid]>target){
                e=mid-1;
            }
            else{
                s=mid+1;
            }
        }
        return ans;
    }

     int lastOccurrence(vector<int>& nums,int target){
        int n = nums.size();
        int s=0;
        int e=n-1;

        int ans=-1;

        while(s<=e){
            int mid=s+(e-s)/2;
            if(nums[mid]==target){
                ans=mid;
                s=mid+1;
            }
            else if(nums[mid]>target){
                e=mid-1;
            }
            else{
                s=mid+1;
            }
        }
        return ans;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        //int n = nums.size();
        vector<int> ans;
        ans.push_back(firstOccurrence(nums,target));
        ans.push_back(lastOccurrence(nums,target));
        return ans;
        
    }
};