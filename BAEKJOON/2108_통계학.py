from collections import Counter
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = sorted([int(input()) for _ in range(N)])
arr = Counter(data).most_common(3)

print(round(sum(data)/N))
print(data[N // 2])
if len(arr) == 1:
    print(arr[0][0])
else:
    print(arr[1][0] if arr[0][1] == arr[1][1] else arr[0][0])
print(data[-1] - data[0])