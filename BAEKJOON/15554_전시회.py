from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    dic[a] = dic[a] + b

items = sorted(dic.items())
answer, dp, pre_key = 0, 0, 0
for i, (key, value) in enumerate(items):
    if i:
        dp = max(value, dp + value - key + pre_key)
    else:
        dp = value
    answer, pre_key = max(answer, dp), key
print(answer)