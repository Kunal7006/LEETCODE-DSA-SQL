class Solution {
public:
    int diameter = 0;

    int height(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        int leftH = height(root->left);
        int rightH = height(root->right);

        diameter = max(diameter, leftH + rightH);

        return 1 + max(leftH, rightH);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return diameter;
    }
};