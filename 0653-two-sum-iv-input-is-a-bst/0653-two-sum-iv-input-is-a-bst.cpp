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
        if(root == NULL){
            return;
        }
        convert(root->left);
        vec.push_back(root->val);
        convert(root->right);
    }
    bool findTarget(TreeNode* root, int k) {
        convert(root);
        int n = vec.size();
        int i =0;
        int j =n-1;
        while(i<j){
            if(vec[i]+vec[j]==k){
                return true;
            }else if(vec[i]+vec[j]<k){
                i++;
            }else{
                j--;
            }
           
        }
        return false;
    }
};