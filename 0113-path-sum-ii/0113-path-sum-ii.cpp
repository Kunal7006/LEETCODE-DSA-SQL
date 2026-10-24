class Solution {
public:
    void dfs(TreeNode* root, int curSum, int targetSum,
             vector<int>& temp, vector<vector<int>>& ans) {
        if (root == NULL) {
            return;
        }

        curSum += root->val;
        temp.push_back(root->val);

        if (!root->left && !root->right) {
            if (curSum == targetSum) {
                ans.push_back(temp);
            }
        }

        dfs(root->left, curSum, targetSum, temp, ans);
        dfs(root->right, curSum, targetSum, temp, ans);

        temp.pop_back();  // Backtrack
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> temp;

        dfs(root, 0, targetSum, temp, ans);

        return ans;
    }
};