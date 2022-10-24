import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [False] * 4
arr[1] = True

for _ in range(N):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
print(arr.index(True))