import sys
def input(): return sys.stdin.readline().strip()

def getArray(str):
    arr = [0] * 4
    for ch in str:
        if ch == 'L':
            arr[0] = arr[0] + 1
        elif ch == 'O':
            arr[1] = arr[1] + 1
        elif ch == 'V':
            arr[2] = arr[2] + 1
        elif ch == 'E':
            arr[3] = arr[3] + 1
    return arr

def getScore(str):
    arr = getArray(str)
    arr = [arr[i] + name_arr[i] for i in range(4)]

    score = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if i == j:
                continue
            score = score * (arr[i] + arr[j]) % 100

    return (-score, str)

name_arr, N = getArray(input()), int(input())
data = [input() for _ in range(N)]
print(min(data, key=getScore))
