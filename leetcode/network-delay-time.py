import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for i in range(n+1)]

        for (a, b, w) in times:
            edges[a].append((b, w))
        
        pq, answer = [(0, k)], [987654321]*(n+1)
        count, max_distance = 0, 0
        while count < n and pq:
            (distance, here) = heapq.heappop(pq)
            if distance >= answer[here]:
                continue
            count += 1
            answer[here], max_distance = distance, max(distance, max_distance)
            for (there, weight) in edges[here]:
                heapq.heappush(pq, (distance + weight, there))
        if count < n:
            return -1
        return max_distance
