import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort()

    answer, temp = 1, data[0][1]
    for i in range(1, N):
        if data[i][1] < temp:
            answer += 1
            temp = data[i][1]

    print(answer)