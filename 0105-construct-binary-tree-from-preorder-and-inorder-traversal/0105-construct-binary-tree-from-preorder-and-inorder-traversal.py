# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,preorder,inorder,start,end):
        if start>end:
            return None
        
        rootVal = preorder[self.idx]
        for i in range(start,end+1):
            if inorder[i]==rootVal:
                break
        
        self.idx+=1
        root = TreeNode(rootVal)
        root.left = self.solve(preorder,inorder,start,i-1)
        root.right = self.solve(preorder,inorder,i+1,end)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        n = len(preorder)

        self.idx =0

        return self.solve(preorder,inorder,0,n-1)
