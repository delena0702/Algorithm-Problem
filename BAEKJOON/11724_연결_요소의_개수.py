import sys
def input(): return sys.stdin.readline().strip()

def get(idx):
    here = idx
    while here != union[here]:
        here = union[here]
    root, here = here, idx
    while here != union[here]:
        union[here], here = root, union[here]
    return root

N, M = map(int, input().split())
union = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    union[get(a)] = get(b)
for i in range(1, N + 1):
    get(i)
print(len(set(union)) - 1)