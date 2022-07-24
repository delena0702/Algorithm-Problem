import sys
def input(): return sys.stdin.readline().strip()


(N, Q, C) = map(int, input().split())
capacity = [0] + list(map(int, input().split()))

cache = 0
undo, redo, now = [], [], -1

for i in range(Q):
    (code, *data) = input().split()
    data = list(map(int, data))
    if code == 'B':
        if undo:
            redo.append(now)
            now = undo.pop()

    elif code == 'F':
        if redo:
            undo.append(now)
            now = redo.pop()

    elif code == 'A':
        for page in redo:
            cache -= capacity[page]
        redo = []
        if now != -1:
            undo.append(now)
        now = data[0]
        cache += capacity[now]
        while undo and cache > C:
            cache -= capacity[undo.pop(0)]

    elif code == 'C':
        for i in range(len(undo)-2, -1, -1):
            if undo[i] == undo[i+1]:
                cache -= capacity[undo.pop(i)]

print(now)

if undo:
    for i in undo[::-1]:
        print(i, end=' ')
    print()
else:
    print(-1)

if redo:
    for i in redo[::-1]:
        print(i, end=' ')
    print()
else:
    print(-1)
