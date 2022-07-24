import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
print("? 1")
sys.stdout.flush()
s = int(input())
print(f"? {N}")
sys.stdout.flush()
e = int(input())
print(f"! {e - s}")
sys.stdout.flush()