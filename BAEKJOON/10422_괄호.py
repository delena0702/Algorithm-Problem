import sys
def input(): return sys.stdin.readline().strip()


MOD = 1_000_000_007

dp = [-1] * 5001


def solve(num):
    if num % 2 == 1:
        return 0
    if num <= 2:
        return 1
    if dp[num] != -1:
        return dp[num]

    answer = 0
    for i in range(0, num, 2):
        answer = (answer + solve(i) * solve(num - i - 2)) % MOD
    dp[num] = answer
    return answer


T = int(input())
for _ in range(T):
    print(solve(int(input())))
