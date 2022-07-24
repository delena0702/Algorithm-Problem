N, M = map(int, input().split())
data = [input() for _ in range(N)]

for length in range(min(N, M), 0, -1):
    for i in range(N - length + 1):
        for j in range(M - length + 1):
            if ([data[i + length - 1][j],
                 data[i][j + length - 1],
                 data[i + length - 1][j + length - 1]
                 ].count(data[i][j]) == 3):
                print(length ** 2)
                exit()