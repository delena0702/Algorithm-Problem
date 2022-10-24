import sys
def input(): return sys.stdin.readline().strip()

while True:
    arr = input().split()
    if arr[0] == '#':
        break
    if int(arr[1]) > 17 or int(arr[2]) >= 80:
        print(arr[0], "Senior")
    else:
        print(arr[0], "Junior")