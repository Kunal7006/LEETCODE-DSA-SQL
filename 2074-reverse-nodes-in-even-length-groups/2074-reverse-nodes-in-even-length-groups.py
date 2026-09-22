# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, last, headOfGroup, n):
        prev = None
        curr = headOfGroup
        nextNode = curr.next
        count = 0

        while curr != None and n > 0:
            nextNode = curr.next

            curr.next = prev
            prev = curr
            curr = nextNode
            n -= 1
            count += 1
        headOfGroup.next = nextNode
        last.next = prev
        return count

    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
        gn = 0
        elementsInPrevGroup = 0
        curr = head
        lastOfPrevGroup = None
        lastOfEvenGroup = None

        while curr != None:
            gn += 1
            if gn % 2 == 0:
                elementsInPrevGroup = self.reverse(lastOfPrevGroup, curr, gn)
                lastOfEvenGroup = curr
                curr = curr.next
            else:
                k = gn
                elementsInPrevgroup = 0
                while curr != None and k > 0:
                    lastOfPrevGroup = curr
                    curr = curr.next
                    k -= 1
                    elementsInPrevGroup += 1

        if gn % 2 == 1 and elementsInPrevGroup % 2 == 0:
            self.reverse(lastOfEvenGroup, lastOfEvenGroup.next, elementsInPrevGroup)
        elif gn % 2 == 0 and elementsInPrevGroup % 2 == 1:
            self.reverse(lastOfPrevGroup, lastOfPrevGroup.next, elementsInPrevGroup)
        return head
