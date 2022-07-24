# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        now = answer = ListNode()
        while head and head.next:
            a, b = head, head.next
            head = head.next.next
            now.next = b
            b.next = a
            now = a

        if head:
            now.next = head
            now = now.next

        now.next = None
        return answer.next
