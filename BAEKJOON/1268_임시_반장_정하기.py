import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
answer = [0 for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for year in range(5):
            if data[i][year] == data[j][year]:
                answer[i], answer[j] = answer[i] + 1, answer[j] + 1
                break

print(answer.index(max(answer)) + 1)