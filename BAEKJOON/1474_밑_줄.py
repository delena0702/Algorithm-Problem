import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

x, remain = divmod(M - sum(map(len, arr)), N - 1)
for i in range(N - 1):
    print(arr[i], end='')
    if remain == 0:
        print('_' * x, end='')
    elif i + remain >= N - 1:
        print('_' * (x + 1), end='')
        remain -= 1
    elif ord(arr[i + 1][0]) > ord('_'):
        print('_' * (x + 1), end='')
        remain -= 1
    else:
        print('_' * x, end='')
print(arr[-1], end='')