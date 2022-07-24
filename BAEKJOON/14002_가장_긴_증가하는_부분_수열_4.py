import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
A = list(map(int, input().split()))

dp, pre = [1]*N, [-1]*N
max_index = 0
for i in range(N):
    for j in range(i):
        if A[j] >= A[i]:
            continue
        if dp[j] + 1 <= dp[i]:
            continue
        dp[i] = dp[j] + 1
        pre[i] = j
    if (dp[max_index] < dp[i]):
        max_index = i

answer = []
here = max_index
while here != -1:
    answer.append(A[here])
    here = pre[here]

print(dp[max_index])
for i in range(dp[max_index] - 1, -1, -1):
    print(answer[i], end=' ')
