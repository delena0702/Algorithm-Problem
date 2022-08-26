N, X = map(int, input().split())
print(*filter(lambda x: x < X, map(int, input().split())))