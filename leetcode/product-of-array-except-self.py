class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        answer = [1]*N

        for i in range(N-1):
            answer[i+1] = answer[i]*nums[i]

        ac = 1
        for i in range(N-1, -1, -1):
            answer[i] *= ac
            ac *= nums[i]
        return answer
