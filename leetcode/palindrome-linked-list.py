# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            slow, slow.next, rev = slow.next, rev, slow
        if fast:
            slow = slow.next
        
        while slow and slow.val == rev.val:
            slow, rev = slow.next, rev.next
        return not slow
