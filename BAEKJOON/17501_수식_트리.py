import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


N = int(input())
arr = sorted([int(input()) for _ in range(N)])
oper = [input().split() for _ in range(N - 1)]
for o in oper:
    o[1], o[2] = int(o[1]), int(o[2])



is_plus = [True for i in range(2 * N)]
queue = deque([2 * N - 1])
while queue:
    here = queue.popleft()

    if here <= N:
        continue

    is_plus[oper[here - N - 1][1]] = is_plus[here]

    if oper[here - N - 1][0] == '+':
        is_plus[oper[here - N - 1][2]] = is_plus[here]
    else:
        is_plus[oper[here - N - 1][2]] = not is_plus[here]

    queue.append(oper[here - N - 1][1])
    queue.append(oper[here - N - 1][2])



plus_count = len(list(filter(lambda x: x, is_plus[1:N+1])))
answer = 0
for i in range(N):
    if i < N - plus_count:
        answer = answer - arr[i]
    else:
        answer = answer + arr[i]
print(answer)