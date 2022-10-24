import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [0] + list(map(int, input().split()))
psum = [0] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    psum[i] = psum[i - 1] + arr[(i + N - 1) % N + 1]

answer = 0
total = psum[N]
for i in range(1, N + 1):
    for j in range(1, N):
        value = psum[i - 1] - psum[i + j - 1]
        if value > 0:
            answer += (value - 1) // total + 1

print(answer)