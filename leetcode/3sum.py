class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer, N = [], len(nums)
        nums.sort()

        for i in range(N-2):
            if i and nums[i] == nums[i-1]:
                continue
            l, r = i+1, N-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    answer.append([nums[i], nums[l], nums[r]])

                if s >= 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return answer
