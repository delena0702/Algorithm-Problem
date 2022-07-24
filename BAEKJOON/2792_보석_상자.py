import sys
def input(): return sys.stdin.readline().strip()


def calc(value):
    global data
    retval = 0
    for d in data:
        retval += (d-1)//value+1
    return retval


(N, M) = map(int, input().split())
data = []
for _ in range(M):
    data.append(int(input()))

l, r = 1, sum(data)
while l < r:
    m = (l + r) // 2
    if N >= calc(m):
        r = m
    else:
        l = m + 1
print(r)
