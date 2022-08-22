import sys
def input(): return sys.stdin.readline().strip()


def get(idx):
    here = idx
    while here != union[here]:
        here = union[here]
    root = here

    here = idx
    while here != union[here]:
        here, union[here] = union[here], root
    return root


N, M = map(int, input().split())
union = [i for i in range(N + 1)]
for _ in range(M):
    o, a, b = map(int, input().split())

    if o == 0:
        union[get(a)] = get(b)

    if o == 1:
        if get(a) == get(b):
            print("YES")
        else:
            print("NO")
