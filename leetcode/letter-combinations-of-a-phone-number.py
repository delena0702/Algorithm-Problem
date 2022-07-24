class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        data = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def dfs(index, s):
            if index == len(digits):
                answer.append(s)
                return
            for ch in data[digits[index]]:
                dfs(index + 1, s + ch)
        if not digits:
            return []
        dfs(0, "")
        return answer
