class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest, answer = 12345, 0

        for price in prices:
            lowest = min(lowest, price)
            answer = max(answer, price - lowest)
        return answer
