from itertools import permutations
from math import sqrt


def getCenter(a, b):
    return a * b / (a + b) * sqrt(2)


data, answer = list(map(int, input().split())), 0

for arr in permutations(data):
    for i in range(8):
        if arr[i] < getCenter(arr[(i + 1) % 8], arr[(i + 7) % 8]):
            break
        if i == 7:
            answer = answer + 1

print(answer)