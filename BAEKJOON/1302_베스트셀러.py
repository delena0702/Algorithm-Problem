from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
counter = defaultdict(int)
for _ in range(N):
    counter[input()] += 1

arr = []
for key, value in counter.items():
    arr.append((-value, key))
arr.sort()
print(arr[0][1])