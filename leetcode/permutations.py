class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(pick, arr):
            if not pick:
                answer.append(arr)
            for i in range(len(pick)):
                dfs(pick[:i]+pick[i+1:], arr + [pick[i]])

        dfs(nums, [])
        return answer
