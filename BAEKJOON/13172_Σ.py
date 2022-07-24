import sys
def input(): return sys.stdin.readline().strip()

def power(num, up):
    if up == 0:
        return 1

    half = power(num, up // 2)
    if up % 2:
        return half * half * num % MOD
    else:
        return half * half % MOD

MOD = 1_000_000_007
M = int(input())
answer = 0
for _ in range(M):
    N, S = map(int, input().split())
    part = S * power(N, MOD - 2) % MOD
    answer = (answer + part) % MOD
print(answer)