import sys
def input(): return sys.stdin.readline().strip()

M = int(input())
s = 0
for _ in range(M):
    query, *arr = input().split()
    arr = list(map(int, arr))

    if query == "add":
        s = s | (1 << arr[0])
    if query == "remove":
        s = s & ~(1 << arr[0])
    if query == "check":
        print((s >> arr[0]) & 1)
    if query == "toggle":
        s = s ^ (1 << arr[0])
    if query == "all":
        s = 0x1fffff
    if query == "empty":
        s = 0