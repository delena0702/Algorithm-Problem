class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for (i, num) in enumerate(nums):
            nums_map[num] = i

        for (i, num) in enumerate(nums):
            if target-num in nums_map and nums_map[target - num] != i:
                return [i, nums_map[target - num]]
