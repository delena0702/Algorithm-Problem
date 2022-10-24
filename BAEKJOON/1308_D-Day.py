from datetime import date
import sys
def input(): return sys.stdin.readline().strip()

arr = [list(map(int, input().split())) for _ in range(2)]
check = True
if date(*arr[1]) >= date(arr[0][0] + 1000, arr[0][1], arr[0][2]):
    print("gg")
else:
    print(f"D-{(date(*arr[1]) - date(*arr[0])).days}")