from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = deque()
for _ in range(N):
    query = input().split()
    if query[0] == "push_front":
        arr.appendleft(int(query[1]))
    elif query[0] == "push_back":
        arr.append(int(query[1]))
    elif query[0] == "pop_front":
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif query[0] == "pop_back":
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif query[0] == "size":
        print(len(arr))
    elif query[0] == "empty":
        print(0 if arr else 1)
    elif query[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif query[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)