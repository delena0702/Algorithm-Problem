import sys
def input(): return sys.stdin.readline().strip()

data = [list(input()) for _ in range(36)]
for arr in data:
    arr[0] = ord(arr[0]) - ord('A')
    arr[1] = int(arr[1]) - 1

dp = [[False] * 6 for _ in range(6)]

for i in range(36):
    a, b = data[i], data[(i + 1) % 36]
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    if dp[a[1]][a[0]]:
        print("Invalid")
        break
    dp[a[1]][a[0]] = True
    if dx and dy and dx + dy == 3:
        continue
    print("Invalid")
    break
else:
    print("Valid")