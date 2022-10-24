import sys
def input(): return sys.stdin.readline().strip()

string = input()
N = len(string)
for i in range(1, N):
    a, b = 1, 1
    for ch in string[:i]:
        a *= int(ch)
    for ch in string[i:]:
        b *= int(ch)
    if a == b:
        print("YES")
        break
else:
    print("NO")