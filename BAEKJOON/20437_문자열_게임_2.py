import sys
import math
def input(): return sys.stdin.readline().strip()


T = int(input())
for i in range(T):
    W, K = input(), int(input())
    indices = [[] for _ in range(26)]

    for j in range(len(W)):
        indices[ord(W[j]) - ord('a')].append(j)
    
    answer = [float('inf'), float('-inf')]
    for j in range(26):
        if len(indices[j]) < K:
            continue
        for k in range(len(indices[j]) - K + 1):
            answer[0] = min(answer[0], indices[j][k + K - 1] - indices[j][k] + 1)
            answer[1] = max(answer[1], indices[j][k + K - 1] - indices[j][k] + 1)

    if math.isinf(answer[0]):
        print("-1")
    else:
        print(*answer, sep=' ')
