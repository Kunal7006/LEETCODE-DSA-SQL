# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head == None or left == right :
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy 
        for i in range(1,left):
            prev = prev.next
        
        curr = prev.next

        for i in range(right-left):

            nextNode = curr.next

            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode
        return dummy.next
