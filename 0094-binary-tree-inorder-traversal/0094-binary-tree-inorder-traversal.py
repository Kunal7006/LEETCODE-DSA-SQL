# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        #morris traversal
        result =[]
        curr = root

        while curr!= None:
            if curr.left == None: # L,v
                result.append(curr.val)
                curr = curr.right
            else:
                leftChild = curr.left

                while leftChild.right!= None:
                    leftChild = leftChild.right
                
                leftChild.right = curr

                # deleting left pointer of curr
                temp = curr
                curr = curr.left

                temp.left = None
        return result
