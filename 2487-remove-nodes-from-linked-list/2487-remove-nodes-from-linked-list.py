# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack=[]
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = stack[-1]
        stack.pop()
        maxNode = curr.val

        resulthead = ListNode(curr.val)

        while stack:
            curr = stack[-1]
            stack.pop()
            if curr.val <maxNode:
                continue
            else:
                newNode = ListNode(curr.val)
                newNode.next = resulthead
                resulthead = newNode
                maxNode = curr.val
        
        return resulthead


        