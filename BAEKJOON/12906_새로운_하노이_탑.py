from collections import deque
import re
import sys
def input(): return sys.stdin.readline().strip()


def move(node, a, b):
    arr = node.split('/')
    if len(arr[a]) == 0:
        return ""
    arr[b] = arr[b] + arr[a][-1]
    arr[a] = arr[a][:-1]
    return '/'.join(arr)


data = [input().split() for _ in range(3)]
for i in range(3):
    data[i] = data[i][1] if int(data[i][0]) else ""
data = '/'.join(data)

visited = set([data])
queue = deque([(data, 0)])
while queue:
    here, distance = queue.popleft()

    if re.match(r'^A*/B*/C*$', here):
        print(distance)
        break

    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            there = move(here, i, j)

            if there == "" or there in visited:
                continue

            visited.add(there)
            queue.append((there, distance + 1))
