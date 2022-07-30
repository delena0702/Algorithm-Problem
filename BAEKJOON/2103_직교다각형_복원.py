from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
dic = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    dic[x].append(y + 20000)
    dic[y + 20000].append(x)

answer = 0
for arr in dic.values():
    arr.sort()
    for i in range(0, len(arr), 2):
        answer = answer + arr[i + 1] - arr[i]
print(answer)