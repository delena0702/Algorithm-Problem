import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

for i in range(N - 2):
    if arr[i] >= arr[i + 1] + arr[i + 2]:
        continue

    print(sum(arr[i:i+3]))
    break
else:
    print(-1)