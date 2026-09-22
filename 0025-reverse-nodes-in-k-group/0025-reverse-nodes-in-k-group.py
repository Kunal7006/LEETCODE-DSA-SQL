# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        curr = head
        prev = None

        while curr != None:
            nextNode = curr.next

            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def getKthNode(self,temp,k):
        k-=1
        while temp != None and k >0:
            temp = temp.next
            k-=1
        return temp
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        temp = head
        prevLast = None

        while temp != None:
            kthNode = self.getKthNode(temp,k)
            if kthNode == None:
                if prevLast:
                    prevLast.next = temp
                break
            
            nextNode = kthNode.next
            kthNode.next = None
            self.reverseLL(temp)
            if temp == head:
                head = kthNode
            else:
                prevLast.next = kthNode
            
            prevLast = temp
            temp = nextNode
        return head