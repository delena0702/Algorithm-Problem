import sys
def input(): return sys.stdin.readline().strip()


(L, C) = map(int, input().split())
data = sorted(input().split())
moum_data = ['a', 'e', 'i', 'o', 'u']


def combination(start, moum, now):
    if len(now) + C - start < L:
        return
    if moum == 0 and len(now) == L:
        return
    if L - moum < 2:
        return
    if len(now) == L:
        print(now)
        return
    combination(start + 1, moum +
                1 if (data[start] in moum_data) else moum, now + data[start])
    combination(start + 1, moum, now)


combination(0, 0, "")
