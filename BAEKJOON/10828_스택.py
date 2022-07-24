import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
stack = []
for _ in range(N):
    query = input().split()
    if query[0] == "push":
        stack.append(int(query[1]))
    elif query[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif query[0] == "size":
        print(len(stack))
    elif query[0] == "empty":
        print(0 if stack else 1)
    elif query[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)