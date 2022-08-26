import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N, dic = int(input()), {}
    for _ in range(N):
        t = input().split()[1]
        dic[t] = dic.get(t, 0) + 1
    answer = 1
    for value in dic.values():
        answer = answer * (value + 1)
    print(answer - 1)
