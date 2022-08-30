import sys
from collections import Counter
def input(): return sys.stdin.readline().strip()


N, data, counter = int(input()),  list(map(int, input().split())), Counter()

for n in data:
    i, arr = 1, []
    while i ** 2 < n:
        if n % i == 0:
            arr.extend([i, n // i])
        i += 1
    if i ** 2 == n:
        arr.append(i)
    counter.update(arr)

max_val = 0
for (value, count) in counter.items():
    if count >= 2:
        max_val = max(max_val, value*count)
print(max_val)
