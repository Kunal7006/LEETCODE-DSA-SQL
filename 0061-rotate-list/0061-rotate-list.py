# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head == None or head.next == None or k ==0:
            return head
        
        temp = head
        d = 1
        while temp.next != None:
            temp = temp.next
            d+=1
        
        k = k % d
        temp.next = head

        end = d-k
        while end:
            temp = temp.next
            end-=1
        head = temp.next
        temp.next = None
        return head