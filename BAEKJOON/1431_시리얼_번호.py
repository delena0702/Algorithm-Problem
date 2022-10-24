import sys
def input(): return sys.stdin.readline().strip()

def getKey(s):
    cnt = 0
    for ch in s:
        if ord('0') <= ord(ch) <= ord('9'):
            cnt += int(ch)
    return (len(s), cnt, s)

N = int(input())
data = [input() for _ in range(N)]
data.sort(key=getKey)
print(*data, sep='\n')