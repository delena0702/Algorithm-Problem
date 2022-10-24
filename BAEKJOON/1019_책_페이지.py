import sys
def input(): return sys.stdin.readline().strip()

def count(x, d):
    while x:
        answer[x % 10] += d
        x //= 10

d = 1
s, e = 1, int(input())
answer = [0] * 10
while s <= e:
    while s <= e and s % 10 != 0:
        count(s, d)
        s += 1

    if s > e:
        break
    
    while s <= e and e % 10 != 9:
        count(e, d)
        e -= 1

    s //= 10
    e //= 10
    for i in range(10):
        answer[i] += (e - s + 1) * d
    d *= 10

print(*answer, sep=' ')