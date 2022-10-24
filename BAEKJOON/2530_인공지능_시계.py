import sys
def input(): return sys.stdin.readline().strip()

A, B, C = map(int, input().split())
D = int(input())

C += D
b, C = divmod(C, 60)
B += b
a, B = divmod(B, 60)
A = (A + a) % 24
print(A, B, C)