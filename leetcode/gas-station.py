class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        N, answer_index, value, g_sum = len(gas), -1, 0, 0
        for i in range(N):
            if value <= 0:
                answer_index = i
            value = max(value, 0) + gas[i] - cost[i]
            g_sum += gas[i] - cost[i]
        return answer_index if g_sum >= 0 else -1


print(Solution().canCompleteCircuit(
    gas=[2, 3, 4], cost=[3, 4, 3]
))
