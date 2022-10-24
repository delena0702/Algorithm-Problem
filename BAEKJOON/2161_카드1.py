from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
queue = deque(range(1, N + 1))
for i in range(N - 1):
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())
print(queue[0])