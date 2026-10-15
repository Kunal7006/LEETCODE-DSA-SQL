# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans =[]
        if root ==None:
            return ans
        
        st =[]
        st.append(root)
        while st:
            curr = st.pop()
            ans.append(curr.val)

            if curr.right!=None:
                st.append(curr.right)
            if curr.left!=None:
                st.append(curr.left)
        return ans
