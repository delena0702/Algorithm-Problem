import sys
def input(): return sys.stdin.readline().strip()

t = 0
while True:
    t += 1
    N = int(input())
    if N == 0:
        break

    print(f"Group {t}")

    data = [input().split() for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(1, N):
            if data[i][j] == 'N':
                print(f"{data[i - j][0]} was nasty about {data[i][0]}")
                cnt += 1
    
    if cnt == 0:
        print("Nobody was nasty")
    print()