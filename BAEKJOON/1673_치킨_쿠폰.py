import sys
def input(): return sys.stdin.readline().strip()

while True:
    try:
        N, K = map(int, input().split())
    except:
        break

    answer = N
    while N >= K:
        answer += N // K
        N = N // K + N % K
        
    print(answer)