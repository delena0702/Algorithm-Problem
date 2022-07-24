import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = [0] + list(map(int, input().split()))
linked = set([1])
for num in data[1:]:
    linked.add(num)

visited, answer = [False] * (N+1), []

for i in range(1, N+1):
    if visited[i]:
        continue
    if i != 1 and i in linked:
        continue
    here = i
    while True:
        answer.append(here)
        if visited[here]:
            break
        else:
            visited[here] = True
            here = data[here]

for i in range(1, N+1):
    if visited[i]:
        continue
    here = i
    while True:
        answer.append(here)
        if visited[here]:
            break
        else:
            visited[here] = True
            here = data[here]

print(len(answer) - 1)
for i in range(1, len(answer)):
    print(answer[i], end=' ')
