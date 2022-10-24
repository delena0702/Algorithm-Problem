import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = [0] * N
j = 0
for i in range(M):
    while j < N and b[i] > a[j] - arr[j]:
        j += 1
    if j == N:
        break

    arr[j] += b[i]
print(sum(a) - sum(arr))