import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))
order = list(range(N))
order.sort(key=lambda i: data[i])

cnt, pre = -1, -1000000001
for i in range(N):
    if pre == data[order[i]]:
        pre = data[order[i]]
        data[order[i]] = cnt
    else:
        pre = data[order[i]]
        cnt += 1
        data[order[i]] = cnt
print(*data, sep=' ')