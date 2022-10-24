import sys
def input(): return sys.stdin.readline().strip()

def dfs(here, remain):
    if remain < 0:
        return float('-inf')
    if here == N:
        return 0
    retval = dfs(here + 1, remain - L[here]) + J[here]
    retval = max(retval, dfs(here + 1, remain))
    return retval

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

print(dfs(0, 99))