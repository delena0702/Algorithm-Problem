from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

N, K = map(int, input().split())
arr = [list(set(input())) for _ in range(N)]
base = set("antic")

if K <= 4:
    print(0)
    exit()

if K == 5:
    answer = 0
    for word in arr:
        if len(word) == 5:
            answer += 1
    print(answer)
    exit()

answer = 0
for chs in combinations("bdefghjklmopqrsuvwxyz", K - 5):
    count = 0
    for word in arr:
        for ch in word:
            if ch not in base and ch not in chs:
                break
        else:
            count += 1
    answer = max(answer, count)
print(answer)