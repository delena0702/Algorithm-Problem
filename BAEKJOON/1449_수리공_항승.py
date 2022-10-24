import sys
def input(): return sys.stdin.readline().strip()

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

r = 0
answer = 0
for i in range(N):
    if arr[i] <= r:
        continue
    r = arr[i] + L - 1
    answer += 1
print(answer)