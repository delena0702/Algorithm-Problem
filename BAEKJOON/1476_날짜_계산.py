data = list(map(int, input().split()))
div = [15, 28, 19]

for i in range(1, 7981):
    for j in range(3):
        if data[j] != (i - 1) % div[j] + 1:
            break
    else:
        print(i)
        break