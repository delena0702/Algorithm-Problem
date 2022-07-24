import bisect

L = int(input())
S = [0] + sorted(list(map(int, input().split())))
n = int(input())
idx = bisect.bisect_left(S, n)

if (S[idx] == n):
    print(0)
else:
    print((n - S[idx - 1]) * (S[idx] - n) - 1)