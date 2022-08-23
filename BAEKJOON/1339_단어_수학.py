from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = [list(input()) for _ in range(N)]
count, change = defaultdict(int), {}

for string in data:
    for i, ch in enumerate(string):
        count[ch] = count[ch] + 10 ** (len(string) - 1 - i)

for i, (ch, _) in enumerate(sorted(count.items(), key=lambda x: x[1], reverse=True)):
    change[ch] = 9 - i

for arr in data:
    for i in range(len(arr)):
        arr[i] = str(change[arr[i]])

print(sum(map(int, map(lambda x: ''.join(x), data))))
