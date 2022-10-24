import sys
def input(): return sys.stdin.readline().strip()

def combine(n, r):
    if r < 0 or r > n:
        return 0

    retval = 1
    for i in range(1, r + 1):
        retval = retval * (n - i + 1) // i
    return retval

def solve(remain, count, end):
    if remain == 0:
        return
    
    for i in range(0, end + 1):
        comb = combine(i, remain - 1)
        if count - comb < 0:
            print(i, end='')
            return solve(remain - 1, count, i + 1)
        count -= comb

N = int(input())
i = 1
for i in range(1, 12):
    comb = combine(10, i)
    if i == 11 or N - comb < 0:
        break
    N -= comb

if i == 11:
    print(-1)
else:
    solve(i, N, 9)