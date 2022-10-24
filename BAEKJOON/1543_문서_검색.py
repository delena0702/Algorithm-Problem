import sys
def input(): return sys.stdin.readline()

a, b = input().replace('\n', ''), input().replace('\n', '')
N, M = len(a), len(b)

i = 0
answer = 0
while i < N - M + 1:
    for j in range(M):
        if a[i + j] != b[j]:
            break
    else:
        answer += 1
        i += max(M, 1)
        continue
    i += 1
print(answer)