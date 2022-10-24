import sys
def input(): return sys.stdin.readline()

N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

for _ in range(K):
    narr = []
    for i in range(len(arr) - 1):
        narr.append(arr[i + 1] - arr[i])
    arr = narr
print(*arr, sep=',')