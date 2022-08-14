from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


N, d, k, c = map(int, input().split())
data = [int(input()) for _ in range(N)]

counter = defaultdict(int)
counter[c] = 1
for i in range(k):
    counter[data[i]] = counter[data[i]] + 1

answer = 0
for i in range(-1, N - 1):
    if i != -1:
        counter[data[i]] = counter[data[i]] - 1
        if counter[data[i]] == 0:
            del counter[data[i]]
        counter[data[(i + k) % N]] = counter[data[(i + k) % N]] + 1
    answer = max(answer, len(counter))
print(answer)
