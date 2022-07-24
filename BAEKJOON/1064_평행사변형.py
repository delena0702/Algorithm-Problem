from math import sqrt


data = list(map(int, input().split()))
data = [data[0:2], data[2:4], data[4:6]]

def length(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if (data[1][0] - data[0][0])*(data[2][1] - data[0][1]) - \
        (data[2][0] - data[0][0])*(data[1][1] - data[0][1]) == 0:
    print(-1.0)
else:
    arr = [length(data[i], data[i+1]) + length(data[i], data[i+2]) for i in range(-2, 1)]
    print(2 * (max(arr) - min(arr)))