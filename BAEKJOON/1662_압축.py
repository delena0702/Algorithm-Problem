import sys
def input(): return sys.stdin.readline().strip()

string = input()
N = len(string)
answer, stack = 0, [1]
for i in range(N):
    if string[i] == '(':
        continue
    if i + 1 < N and string[i + 1] == '(':
        stack.append(stack[-1] * int(string[i]))
        continue
    if string[i] == ')':
        stack.pop()
        continue
    answer += stack[-1]
print(answer)