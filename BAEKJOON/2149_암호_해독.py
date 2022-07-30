import sys
def input(): return sys.stdin.readline().strip()

key, data = input(), input()
N, M = len(data), len(key)

order = [i for i in range(M)]
order.sort(key=lambda x: key[x])

answer = ['_'] * N
for i, ch in enumerate(data):
    x, y = divmod(i, N // M)
    answer[M * y + order[x]] = ch
print(''.join(answer))