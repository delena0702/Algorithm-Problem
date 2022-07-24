class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if len(expression) <= 2:
            return [int(expression)]

        retval = []
        for (i, ch) in enumerate(expression):
            if ch not in "+-*":
                continue

            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i+1:])
            retval += [eval(str(l) + ch + str(r)) for l in left for r in right]
        return retval
