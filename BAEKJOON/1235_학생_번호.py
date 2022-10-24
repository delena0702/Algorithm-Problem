import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [input() for _ in range(N)]
K = len(arr[0])

s, e = 1, K
while s < e:
    m = (s + e) // 2
    ss = set(map(lambda x: x[-m:], arr))
    if len(ss) == N:
        e = m
    else:
        s = m + 1
print(s)