from bisect import bisect_left
import sys
def input(): return sys.stdin.readline().strip()

string = input()
N = len(string)

z = [0] * N
l, r = 0, 0
for i in range(1, N):
    if i <= r:
        z[i] = min(z[i - l], r - i + 1)

    while i + z[i] < N and string[z[i]] == string[i + z[i]]:
        z[i] += 1

    if r < i + z[i] - 1:
        l, r = i, i + z[i] - 1
z[0] = N

arr = z[:]
arr.sort()

answer = []
for i in range(N - 1, -1, -1):
    if i + z[i] != N:
        continue
    answer.append((N - i, N - bisect_left(arr, z[i])))

print(len(answer))
for i in range(len(answer)):
    print(*answer[i])