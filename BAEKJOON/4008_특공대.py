from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

def a1(j):
    return -2 * a * psum[j]
def a0(j):
    return a * (psum[j] ** 2) - b * psum[j] + dp[j]
def f(num):
    return a * (num ** 2) + b * num + c

N = int(input())
a, b, c = map(int, input().split())
data = [0] + list(map(int, input().split()))
psum = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] + data[i]

dp = [0] * (N + 1)
queue = deque([(0, float('-inf'))])
for i in range(1, N + 1):
    while len(queue) >= 2 and queue[1][1] <= psum[i]:
        queue.popleft()

    j = queue[0][0]
    dp[i] = f(psum[i] - psum[j]) + dp[j]

    while True:
        j = queue[-1][0]
        xpos = - (a0(i) - a0(j)) / (a1(i) - a1(j))
        if queue[-1][1] <= xpos:
            break
        queue.pop()
    queue.append((i, xpos))

print(dp[N])