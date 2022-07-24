S = list(map(int, input().split()))

counter = {}
for i in range(1, S[0] + 1):
    for j in range(1, S[1] + 1):
        for k in range(1, S[2] + 1):
            sum_value = i + j + k
            counter[sum_value] = counter.get(sum_value, 0) + 1

maximum = 0
for key, value in counter.items():
    if (value > maximum):
        maximum = value
    else:
        print(key - 1)
        break