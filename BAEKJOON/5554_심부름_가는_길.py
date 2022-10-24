import sys
def input(): return sys.stdin.readline().strip()

arr = [int(input()) for _ in range(4)]
print(*divmod(sum(arr), 60), sep='\n')