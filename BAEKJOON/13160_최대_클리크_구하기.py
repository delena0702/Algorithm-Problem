from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dic = defaultdict(lambda: [0, 0])
for s, e in data:
    dic[s][0] = dic[s][0] + 1
    dic[e][1] = dic[e][1] + 1

cnt = 0
max_idx, max_value = -1, -1
for num, arr in sorted(dic.items()):
    cnt = cnt + arr[0]
    if max_value < cnt:
        max_idx, max_value = num, cnt
    cnt = cnt - arr[1]

print(max_value)
for i in range(N):
    if max_idx < data[i][0] or max_idx > data[i][1]:
        continue
    print(i + 1, end=' ')
print()
