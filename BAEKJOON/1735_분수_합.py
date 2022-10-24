from math import gcd
import sys
def input(): return sys.stdin.readline().strip()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = [0, 0]
answer[0] = a[0] * b[1] + a[1] * b[0]
answer[1] = a[1] * b[1]

g = gcd(*answer)
print(answer[0] // g, answer[1] // g)