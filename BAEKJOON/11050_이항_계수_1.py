from math import factorial
import sys
def input(): return sys.stdin.readline().strip()

N, K = map(int, input().split())
print(factorial(N) // factorial(K) // factorial(N - K))