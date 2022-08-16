import sys
def input(): return sys.stdin.readline().strip()


def get(idx):
    root, here = idx, idx
    while root != union[root][0]:
        root = union[root][0]
    while here != union[here][0]:
        union[here][0], here = root, union[here][0]
    return root


N, L = map(int, input().split())
union = [[i, False] for i in range(L + 1)]

for i in range(1, N + 1):
    a, b = map(int, input().split())
    check = True

    if get(a) == a and not union[a][1]:
        union[a] = [get(b), True]
    elif get(b) == b and not union[b][1]:
        union[b] = [get(a), True]
    elif not union[get(a)][1]:
        union[get(a)] = [get(b), True]
    elif not union[get(b)][1]:
        union[get(b)] = [get(a), True]
    else:
        check = False

    print("LADICA" if check else "SMECE")
