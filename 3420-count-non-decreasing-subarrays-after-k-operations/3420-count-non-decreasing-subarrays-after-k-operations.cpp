
class Solution {
public:
    typedef long long ll;

    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int r = n - 1;

        deque<pair<int,int>> dq;

        ll op = 0;
        ll result = 0;

        for(int l = n - 1; l >= 0; l--) {
            int nsize = 1;

            while(!dq.empty() && nums[l] >= dq.back().first) {
                auto [height, size] = dq.back();
                dq.pop_back();

                op += 1LL * (nums[l] - height) * size;
                nsize += size;
            }

            dq.push_back({nums[l], nsize});

            while(op > k) {
                op -= dq.front().first - nums[r];
                dq.front().second -= 1;

                if(dq.front().second == 0) {
                    dq.pop_front();
                }

                r -= 1;
            }

            result += r - l + 1;
        }

        return result;
    }
};
