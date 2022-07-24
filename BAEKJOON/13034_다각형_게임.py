import sys
def input(): return sys.stdin.readline().strip()


N = int(input())

dp = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    s = set()
    for j in range((i - 2) // 2 + 1):
        s.add(dp[j] ^ dp[i - j - 2])
    for j in range(100):
        if j in s:
            continue
        dp[i] = j
        break
print(1 if dp[N] else 2)
