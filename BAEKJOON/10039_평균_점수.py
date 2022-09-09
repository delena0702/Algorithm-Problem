data = [int(input()) for _ in range(5)]
print(sum(map(lambda x: max(40, x), data)) // 5)