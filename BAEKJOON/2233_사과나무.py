import sys
def input(): return sys.stdin.readline().strip()


N, data = int(input()), input()
X, Y = map(int, input().split())
stack, paths, nodes = [], [], {}

for i in range(1, 2*N + 1):
    ch = data[i - 1]

    if i in [X, Y] and ch == '1':
        paths.append(stack[:])
        if X == Y:
            paths.append(stack[:])

    if ch == '0':
        stack.append(i)
    else:
        nodes[stack.pop()] = i

    if i in [X, Y] and ch == '0':
        paths.append(stack[:])
        if X == Y:
            paths.append(stack[:])

for i in range(min(len(paths[0]), len(paths[1]))):
    if paths[0][i] != paths[1][i]:
        print(paths[0][i - 1], nodes[paths[0][i - 1]])
        break
else:
    print(paths[0][i], nodes[paths[0][i]])
