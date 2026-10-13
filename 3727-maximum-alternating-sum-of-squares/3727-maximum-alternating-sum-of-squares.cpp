class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();

        vector<int> temp;
        for(int &num:nums){
            temp.push_back(abs(num));
        }
        sort(temp.begin(),temp.end());

        int low =0;
        int high = n-1;

        long long ans = 0;

        while(low<high){
            ans = ans + 1LL*temp[high]*temp[high] - 1LL*temp[low]*temp[low];
            low++;
            high--;
        }

        if(n%2==1){
            //low++;
            ans += 1LL* temp[low]*temp[low];
        }

        return ans;


    }
};