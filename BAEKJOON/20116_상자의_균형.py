import sys
def input(): return sys.stdin.readline().strip()


(N, L) = map(int, input().split())
x = list(map(int, input().split()))

answer, sum = "stable", x[N - 1]
for i in range(N - 2, -1, -1):
    if abs(sum / (N - i - 1) - x[i]) >= L:
        answer = "unstable"
        break
    sum += x[i]
print(answer)
