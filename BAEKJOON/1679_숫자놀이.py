import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

dp = [0]

i = 1
while True:
    ndp = K + 1
    for j in range(N):
        if i - arr[j] >= 0:
            ndp = min(ndp, dp[i - arr[j]] + 1)
    if ndp > K:
        break
    dp.append(ndp)
    i += 1

if i % 2:
    print(f"jjaksoon win at {i}")
else:
    print(f"holsoon win at {i}")