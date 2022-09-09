from itertools import permutations

N = int(input())
for arr in permutations(range(1, N + 1), N):
    print(*arr)