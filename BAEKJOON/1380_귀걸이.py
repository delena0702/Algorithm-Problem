import sys
def input(): return sys.stdin.readline().strip()

t = 0
while True:
    t += 1
    N = int(input())
    if N == 0:
        break

    names = [input() for _ in range(N)]
    data = [input().split() for _ in range(2 * N - 1)]
    count = [0] * N

    for num, ch in data:
        num = int(num)
        count[num - 1] += 1
    for i in range(N):
        if count[i] == 1:
            print(t, names[i])
            break