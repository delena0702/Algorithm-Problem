import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))
S = int(input())

answer = 0
for num in data:
    answer += (num + S - 1) // S * S
print(answer)