# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next ==None:
            return 
        
        slow = head
        fast = head

        while fast !=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = None

        slow.next = None

        while curr!=None:
            nxt = curr.next

            curr.next = prev

            prev = curr
            curr = nxt
        
        first = head 
        second = prev

        while second!=None:
            firstNext = first.next
            secondNext = second.next

            first.next = second
            second.next = firstNext

            first=firstNext
            second= secondNext