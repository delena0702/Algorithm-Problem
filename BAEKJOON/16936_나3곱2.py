input()
def rank(n, m):
    answer = 0
    while n % m == 0:
        n, answer = n // m, answer + 1
    return answer

print(*sorted(list(map(int, input().split())), key=lambda x: (-rank(x, 3), rank(x, 2))), sep=' ')