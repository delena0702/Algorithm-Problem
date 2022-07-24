N = int(input())
data = [list(map(lambda x: x == 'Y', input())) for _ in range(N)]
if N == 1:
    print(0)
    exit()
print(max(*map(lambda x: x.count(True), [[([data[i][j] and data[j][k] for j in range(N)].count(True) > 0 or data[i][k]) and i != k for k in range(N)] for i in range(N)])))
