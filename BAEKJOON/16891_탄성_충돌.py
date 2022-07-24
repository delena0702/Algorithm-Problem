from fractions import Fraction

N = int(input())

v, answer = [Fraction(0), Fraction(-1)], 0
m = [
    [Fraction(1 - N*N, 1 + N*N), Fraction(2*N*N, 1 + N*N)],
    [Fraction(2, 1 + N*N), Fraction(-1 + N*N, 1 + N*N)]
]
while v[1] < v[0]:
    v = [sum([m[i][j] * v[j] for j in range(2)]) for i in range(2)]
    answer = answer + 1

    if v[0] < 0:
        v[0] = -v[0]
        answer = answer + 1

print(answer)