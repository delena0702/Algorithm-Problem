class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack, retval = [], [0] * len(temperatures)

        for (i, t) in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                l = stack.pop()
                retval[l] = i - l
            stack.append(i)
        return retval
