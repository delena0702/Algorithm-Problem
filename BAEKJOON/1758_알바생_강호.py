import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

answer = 0
for i in range(N):
    answer += max(arr[i] - i, 0)
print(answer)