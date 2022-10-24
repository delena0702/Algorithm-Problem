import sys
def input(): return sys.stdin.readline().strip()

arr = [int(input()) for _ in range(5)]
print(min(arr[:3]) + min(arr[3:]) - 50)