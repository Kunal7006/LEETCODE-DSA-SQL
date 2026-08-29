class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        
        vector<vector<int>> groups;
        unordered_map<int, int> numToGroup;

        // Sort the array
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());

        // Create groups
        for (int n : sortedNums) {

            if (groups.empty() ||
                abs(n - groups.back().back()) > limit) {
                
                groups.push_back(vector<int>());
            }

            groups.back().push_back(n);

            numToGroup[n] = groups.size() - 1;
        }

        // Pointer for each group
        vector<int> index(groups.size(), 0);

        vector<int> res;

        // Process original array
        for (int n : nums) {

            int group = numToGroup[n];

            res.push_back(groups[group][index[group]]);

            index[group]++;
        }

        return res;
    }
};