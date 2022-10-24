import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_price, max_val = 0, 0

for i in range(N):
    price = arr[i][0]
    total = 0

    for j in range(N):
        if arr[j][0] >= price:
            total += max(price - arr[j][1], 0)
    
    if total > max_val or (total == max_val and price < max_price):
        max_price = price
        max_val = total
print(max_price)