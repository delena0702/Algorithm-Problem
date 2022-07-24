N = int(input())
data = list(map(int, input().split()))

y = sum(map(lambda x: (x // 30) * 10 + 10, data))
m = sum(map(lambda x: (x // 60) * 15 + 15, data))

if (y <= m):
    print("Y", end=' ')
if (m <= y):
    print("M", end=' ')
print(min(y, m))