import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(range(N))
count, idx, check = 0, -1, [False] * N

while count < 2 * (N - 1):
    idx = (idx + 1) % N
    while check[idx]:
        idx = (idx + 1) % N

    count = count + 1
    if count % 2:
        check[idx] = True
        
if N == 1:
    print(1)
else:
    print(idx + 1)