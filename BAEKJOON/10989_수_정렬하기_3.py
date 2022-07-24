import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
cnt = [0] * 10001
for _ in range(N):
    num = int(input())
    cnt[num] = cnt[num] + 1

for i in range(1, 10001):
    for j in range(cnt[i]):
        print(i)