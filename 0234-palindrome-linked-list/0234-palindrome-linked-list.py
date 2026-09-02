# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev = None
        curr = head

        while curr != None:
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        slow = self.reverseLL(slow)

        fast = head
        while slow != None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
