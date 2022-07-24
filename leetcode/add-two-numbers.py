class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        answer = ListNode()
        now = answer
        while l1 or l2 or carry:
            (carry, n) = divmod(
                carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            now.next = ListNode(n)
            now = now.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return answer.next
