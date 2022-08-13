from functools import cmp_to_key
from math import ceil, sqrt
import sys
def input(): return sys.stdin.readline().strip()
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def ccw(a, b): return a[0] * b[1] - a[1] * b[0]
def cmp(a, b):
    a, b = sub(a, pivot), sub(b, pivot)
    cp = -ccw(a, b)
    if cp:
        return cp
    return a[0] ** 2 + a[1] ** 2 - b[0] ** 2 - b[1] ** 2

case = 1
while True:
    n = int(input())
    if n == 0:
        break
    data = [tuple(map(int, input().split())) for _ in range(n)]

    pivot = min(data)
    queue = list(filter(lambda x: x != pivot, data))
    queue.sort(key=cmp_to_key(cmp))
    stack = [pivot]
    for p in queue:
        while len(stack) >= 2 and ccw(sub(stack[-1], stack[-2]), sub(p, stack[-1])) <= 0:
            stack.pop()
        stack.append(p)
    data, n = stack, len(stack)

    answer = float('inf')
    for i in range(-1, n - 1):
        length = 0
        for j in range(i + 2 - n, i):
            a, b = sub(data[i + 1], data[i]), sub(data[j], data[i])
            l = ccw(a, b) / sqrt(a[0] ** 2 + a[1] ** 2)
            length = max(length, abs(l))

        else:
            answer = min(answer, length)
    print(f"Case {case}: {ceil(answer * 100) / 100:.2f}")
    case = case + 1
