def solve(n, r, c):
    if n == 0:
        return 0
    next_length = 2 ** (n - 1)
    step = 2 * (r // next_length) + (c // next_length)
    return solve(n - 1, r % next_length, c % next_length) + step * (next_length ** 2)

N, R, C = map(int, input().split())
print(solve(N, R, C))