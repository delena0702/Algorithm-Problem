import sys
def input(): return sys.stdin.readline().strip()
T = int(input())

def isInCircle(cx, cy, cr, x, y):
    return (cx -x)**2 + (cy - y)**2 - cr**2

while (T):
    T -= 1
    (x1,y1,x2,y2) = map(int, input().split())
    N = int(input())
    
    answer = 0
    for i in range(N):
        (x, y, r) = map(int, input().split())
        (a, b) = (isInCircle(x, y, r, x1, y1), isInCircle(x, y, r, x2, y2))
        if (a*b <= 0):
            answer += 1
    print(answer)