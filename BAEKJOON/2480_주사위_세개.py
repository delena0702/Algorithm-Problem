from itertools import combinations

data = list(map(int, input().split()))
count, same_number = 0, 0
for a, b in combinations(data, 2):
    if a == b:
        count, same_number = count + 1, a

if count == 0:
    print(max(data) * 100)
elif count == 1:
    print(1000 + same_number * 100)
else:
    print(10000 + same_number * 1000)
