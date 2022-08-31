from itertools import permutations
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))
answer = 0
for arr in permutations(data):
    temp = 0
    for i in range(N - 1):
        temp = temp + abs(arr[i] - arr[i + 1])
    answer = max(answer, temp)
print(answer)