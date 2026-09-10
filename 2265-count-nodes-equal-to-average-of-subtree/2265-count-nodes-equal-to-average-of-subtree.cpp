/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0;

    pair<int, int> dfs(TreeNode* root) {
        if (root == nullptr) {
            return {0, 0};   // {sum, count}
        }

        // Get left subtree sum and count
        auto left = dfs(root->left);

        // Get right subtree sum and count
        auto right = dfs(root->right);

        // Calculate current subtree sum and count
        int sum = root->val + left.first + right.first;
        int count = 1 + left.second + right.second;

        // Calculate average
        int average = sum / count;

        // Check if current node equals average
        if (root->val == average) {
            ans++;
        }

        return {sum, count};
    }

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};