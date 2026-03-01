# 61. Rotate List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev