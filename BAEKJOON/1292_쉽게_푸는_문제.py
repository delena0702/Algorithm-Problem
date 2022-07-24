from math import sqrt
def square_sum(x):
    return x * (x + 1) * (2 * x + 1)// 6

A, B = map(int, input().split())
values = int(1 + sqrt(8 * A - 7)) // 2, int(1 + sqrt(8 * B - 7)) // 2
end, start = values[0] * (values[0] + 1) // 2, values[1] * (values[1] - 1) // 2 + 1
print(values[0] * (end - A + 1) +\
    values[1]*(B - start + 1) +\
    square_sum(values[1] - 1) - square_sum(values[0]))