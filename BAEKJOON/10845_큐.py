from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
queue = deque()
for _ in range(N):
    query = input().split()
    if query[0] == "push":
        queue.append(int(query[1]))
    elif query[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif query[0] == "size":
        print(len(queue))
    elif query[0] == "empty":
        print(0 if queue else 1)
    elif query[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif query[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)