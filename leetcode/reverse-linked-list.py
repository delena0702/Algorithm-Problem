# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            head.next, head, rev = rev, head.next, head
        return rev
