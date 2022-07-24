import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
i, count = 1, [0]
dp = [0] * (N+1)
while True:
    count.append(i*(i+1)*(i+2)//6)
    if count[i] > N:
        break
    i += 1

for now in range(1, N+1):
    dp[now] = now

    j = 1
    while count[j] <= now:
        dp[now] = min(dp[now], dp[now - count[j]] + 1)
        j += 1

print(dp[N])
