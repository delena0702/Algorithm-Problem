from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
data = [input() for _ in range(N)]

answer = defaultdict(int)
for i in range(N):
    for j in range(M):
        answer[data[i][j]] += (i + 1) * (2 * N - i) * (j + 1) * (2 * M - j)
        answer[data[i][j]] += (N + i + 1) * (N - i) * (j + 1) * (2 * M - j)
        answer[data[i][j]] += (i + 1) * (2 * N - i) * (M + j + 1) * (M - j)
        answer[data[i][j]] += (N + i + 1) * (N - i) * (M + j + 1) * (M - j)

for i in range(ord('A'), ord('Z') + 1):
    print(answer[chr(i)])