class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(pq, (lists[i].val, i))
            lists[i] = lists[i].next

        retval = here = ListNode()
        while pq:
            (val, index) = heapq.heappop(pq)
            here.next = ListNode(val)
            here = here.next

            if lists[index]:
                heapq.heappush(pq, (lists[index].val, index))
                lists[index] = lists[index].next

        return retval.next
