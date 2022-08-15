import sys
def input(): return sys.stdin.readline().strip()

def update(a, b, w):
    pa, wa = get(a)
    pb, wb = get(b)
    weight[pb] = [pa, w + wa - wb]

def get(idx):
    root, total_w = idx, 0
    while root != weight[root][0]:
        total_w, root = total_w + weight[root][1], weight[root][0]
    
    here, w = idx, 0
    while here != weight[here][0]:
        weight[here][1], w = total_w - w, w + weight[here][1]
        weight[here][0], here = root, weight[here][0]
    return weight[idx]


while True:
    N, M = map(int, input().split())
    if N == 0:
        break

    weight = [[i, 0] for i in range(N + 1)]
    for i in range(M):
        query = input().split()
        if query[0] == '!':
            update(int(query[1]), int(query[2]), int(query[3]))
        else:
            a, b = get(int(query[1])), get(int(query[2])) 
            if a[0] == b[0]:
                print(b[1] - a[1])
            else:
                print("UNKNOWN")