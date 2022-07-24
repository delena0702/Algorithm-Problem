class Solution:
    def trap(self, height: list[int]) -> int:
        answer = 0
        stack = []

        for (i, h) in enumerate(height):
            while stack and stack[-1][1] < h:
                (j, h0) = stack.pop()

                if len(stack) == 0:
                    break

                answer += (i - stack[-1][0] - 1)*(min(h, stack[-1][1]) - h0)

            stack.append((i, h))
        return answer

