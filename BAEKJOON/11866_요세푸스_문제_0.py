import sys
def input(): return sys.stdin.readline().strip()

N, K = map(int, input().split())
data = list(range(1, N + 1))
answer = []
here = 0

print("<", end='')
while data:
    here = (here + K - 1) % len(data)
    if len(data) == 1:
        print(data.pop(here), end='>')
    else:
        print(data.pop(here), end=', ')