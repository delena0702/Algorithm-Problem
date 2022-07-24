import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = []

for num in arr:
    is_continue = False

    for i in range(len(dp)):
        if num >= dp[i]:
            dp[i] = dp[i] + 1
            is_continue = True
            break

    if is_continue:
        continue

    dp.append(1)

print(len(dp))
