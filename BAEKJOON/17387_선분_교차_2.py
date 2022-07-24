import sys
def input(): return sys.stdin.readline().strip()

def ccw(p1, p2, p3):
    return (p2[0]-p1[0]) * (p3[1]-p1[1]) - \
        (p2[1]-p1[1]) * (p3[0]-p1[0])

def check(a, b, c, d):
    return (c-a)*(d-a) <= 0 or (c-b)*(d-b) <= 0 or (b-c)*(a-c) <= 0

arr = [list(map(int, input().split())) for i in range(2)]
arr = [arr[0][0:2], arr[0][2:4], arr[1][0:2], arr[1][2:4]]

result = (ccw(arr[0], arr[1], arr[2]), ccw(arr[0], arr[1], arr[3]))

# 한 직선 상에 있는 경우
if result[0] == 0 and result[1] == 0:
    if (arr[0][0] == arr[1][0]):
        print("1" if check(arr[0][1], arr[1][1], arr[2][1], arr[3][1]) else "0")
    else:
        print("1" if check(arr[0][0], arr[1][0], arr[2][0], arr[3][0]) else "0")

elif (result[0] * result[1] > 0):
    print("0")
    
else:
    result = (ccw(arr[2], arr[3], arr[0]), ccw(arr[2], arr[3], arr[1]))
    print("1" if result[0] * result[1] <= 0 else "0")