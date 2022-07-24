from collections import deque
from itertools import combinations, permutations
import sys
def input(): return sys.stdin.readline().strip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isValid(indices):
    remain = set(indices)
    queue = deque([indices[0]])
    while queue:
        here = queue.popleft()
        y, x = divmod(here, N)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if ny * N + nx not in remain:
                continue
            remain.remove(ny * N + nx)
            queue.append(ny * N + nx)

    return len(remain) == 0

def getLength(indices):
    retval = float('inf')
    for order in permutations(range(count), count):
        temp = 0
        for i in range(count):
            temp = temp + abs(arr[i] // N - indices[order[i]] // N) + abs(arr[i] % N - indices[order[i]] % N)
        retval = min(retval, temp)
    return retval

N = 5
data = [list(map(lambda x: x == '*', input())) for _ in range(5)]
count = sum(map(lambda x: x.count(True), data))

if count == 1:
    print(0)
    exit()

arr = []
for i in range(N):
    for j in range(N):
        if data[i][j]:
            arr.append(i * N + j)

answer = float('inf')
for indices in combinations(list(range(N*N)), count):
    if not isValid(indices):
        continue
    answer = min(answer, getLength(indices))
print(answer)
    