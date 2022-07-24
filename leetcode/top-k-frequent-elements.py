class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda x: x[0], list(Counter(nums).most_common(k))))