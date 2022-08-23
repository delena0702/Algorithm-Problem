data, answer = [list(map(int, input().split())) for _ in range(3)], [0, 0]

for i in range(2):
    for j in range(2):
        for k in range(j + 1, 3):
            if data[j][i] == data[k][i]:
                answer[i] = data[3 - j - k][i]

print(*answer, sep=' ')
