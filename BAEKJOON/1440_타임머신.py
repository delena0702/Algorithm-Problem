import sys
def input(): return sys.stdin.readline().strip()

times = list(map(int, input().split(":")))

cnt2 = len([time for time in times if 0 <= time <= 59])
cnt = len([time for time in times if 1 <= time <= 12])
if cnt2 == 3:
    print(2 * cnt)
else:
    print(0)