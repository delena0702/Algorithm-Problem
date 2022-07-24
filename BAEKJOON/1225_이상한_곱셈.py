from itertools import combinations


A, B = map(lambda x: list(map(int, x)), input().split())

answer = 0
for i in range(len(A)):
    for j in range(len(B)):
        answer = answer + A[i] * B[j]
print(answer)