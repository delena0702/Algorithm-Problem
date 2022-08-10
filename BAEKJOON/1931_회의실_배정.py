import sys
sys.stdin = open('1.txt')
def input(): return sys.stdin.readline().strip()


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()

answer, bound = 0, -1
for s, e in data:
    if s >= bound:
        answer, bound = answer + 1, e
    else:
        bound = min(bound, e)
print(answer)
