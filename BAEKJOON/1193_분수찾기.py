from math import ceil, sqrt


X = int(input())
sum_value = ceil((sqrt(1 + 8 * X) - 1) / 2) + 1
index = X - (sum_value - 2) * (sum_value - 1) // 2
if sum_value % 2:
    print("{}/{}".format(index, sum_value - index))
else:
    print("{}/{}".format(sum_value - index, index))