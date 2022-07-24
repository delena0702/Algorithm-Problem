import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


source, target = list(input()), list(input())
N = len(source)

if (''.join(sorted(source)) != ''.join(sorted(target))):
    print("-1")
    exit()

index, answer = N - 1, 0

for i in range(N - 1, -1, -1):
    if source[i] == target[index]:
        index = index - 1

print(index + 1)
