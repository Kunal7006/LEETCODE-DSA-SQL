class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        # Step 1: Detect whether a cycle exists
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # Loop ended normally -> no cycle
            return None

        # Step 2: Find the beginning of the cycle
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow