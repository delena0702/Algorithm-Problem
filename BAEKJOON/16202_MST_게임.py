import sys
def input(): return sys.stdin.readline().strip()


def get(x):
    here = x
    while here != union[here]:
        here = union[here]
    while x != union[x]:
        x, union[x] = union[x], here
    return here


N, M, K = map(int, input().split())

edges = []
for i in range(1, M + 1):
    x, y = map(int, input().split())
    edges.append((i, x, y))

check = False
for i in range(K):
    if check:
        print(0, end=' ')
        continue

    answer, cnt = 0, 0
    union = [i for i in range(N + 1)]

    for j in range(i, len(edges)):
        weight, a, b = edges[j]

        if get(a) == get(b):
            continue

        union[get(a)] = get(b)
        cnt = cnt + 1
        answer = answer + weight

    if cnt == N - 1:
        print(answer, end=' ')
    else:
        check = True
        print(0, end=' ')
print()
