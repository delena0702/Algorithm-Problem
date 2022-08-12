import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))

order = [0] * (N + 1)
for i in range(N):
    order[data[i]] = i

check = [False] * (N + 1)
check[0] = True

for i in range(N):
    if check[data[i]] or check[data[i] - 1]:
        continue

    if order[data[i] - 1] < i:
        continue
    
    check[data[i]] = check[data[i] - 1] = True
    data[order[data[i] - 1]] = data[i]
    data[i] = data[i] - 1
print(*data, sep=' ')