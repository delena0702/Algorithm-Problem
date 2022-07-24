from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

def area(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

T = int(input())
for i in range(T):
    N = int(input())
    check = set()
    data = [tuple(map(int, input().split())) for _ in range(N)]
    for pos in data:
        check.add(pos)
    
    maximum = 0
    for arr in combinations(data, 2):
        if area(arr[0], arr[1]) <= maximum:
            continue
        dx, dy = arr[1][0] - arr[0][0], arr[1][1] - arr[0][1]
        if (arr[0][0] + dy, arr[0][1] - dx) in check and (arr[1][0] + dy, arr[1][1] - dx) in check:
            maximum = area(arr[0], arr[1])
            
    print(maximum)