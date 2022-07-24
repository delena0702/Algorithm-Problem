import sys
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
min_cost = list(map(int, input().split()))
for _ in range(M - 1):
    (a, b) = map(int, input().split())
    min_cost = [min(a, min_cost[0]), min(b, min_cost[1])]

if min_cost[0] >= min_cost[1]*6:
    print(min_cost[1] * N)
else:
    print(min_cost[0] * (N // 6) + min(min_cost[0], min_cost[1] * (N % 6)))
