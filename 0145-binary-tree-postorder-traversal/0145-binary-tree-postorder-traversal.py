# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans =[]

        if root == None:
            return ans
        
        st1 =[]
        st2 =[]
        st1.append(root)

        while st1:
            curr = st1.pop()
            st2.append(curr)

            if curr.left!=None:
                st1.append(curr.left)
            if curr.right!=None:
                st1.append(curr.right)
        
        while st2:
            ans.append(st2.pop().val)
        return ans

        