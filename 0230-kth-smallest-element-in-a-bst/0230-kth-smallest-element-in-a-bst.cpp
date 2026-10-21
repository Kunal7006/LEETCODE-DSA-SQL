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
    vector<int> vec;
    void convert(TreeNode* root){
        if(root==NULL){
            return;
        }
        convert(root->left);
        vec.push_back(root->val);
        convert(root->right);
    }
    int kthSmallest(TreeNode* root, int k) {
        convert(root);
        return vec[k-1];
    }
};