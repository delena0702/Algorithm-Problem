import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
stack, answer = [], 0
for i in range(N+1):
    if i == N:
        height = 0
    else:
        (_, height) = map(int, input().split())

    recent_height = 0
    while stack and stack[-1] > height:
        if (recent_height != stack[-1]):
            answer += 1
        recent_height = stack.pop()

    if i == N:
        break

    stack.append(height)
print(answer)
