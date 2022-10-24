from collections import defaultdict
import sys

counter = defaultdict(int)
while True:
    string = sys.stdin.read()
    if len(string) == 0:
        break

    for ch in string:
        if ch == ' ' or ch == '\n':
            continue
        counter[ch] += 1

arr = []
for ch, value in counter.items():
    arr.append((-value, ch))
arr.sort()

for i in range(len(arr)):
    if arr[0][0] == arr[i][0]:
        print(arr[i][1], end='')
        continue
    break