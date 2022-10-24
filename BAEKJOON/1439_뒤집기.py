import sys
def input(): return sys.stdin.readline().strip()

S = input()
N = len(S)
cnt = 0
for i in range(N - 1):
    if S[i] != S[i + 1]:
        cnt += 1
print((cnt + 1) // 2)