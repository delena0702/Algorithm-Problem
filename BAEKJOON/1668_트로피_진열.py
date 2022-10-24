import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [int(input()) for _ in range(N)]
answer = [0, 0]

maximum = float('-inf')
for i in range(N):
    if arr[i] > maximum:
        maximum = arr[i]
        answer[0] += 1

maximum = float('-inf')
for i in range(N - 1, -1, -1):
    if arr[i] > maximum:
        maximum = arr[i]
        answer[1] += 1

print(*answer, sep='\n')