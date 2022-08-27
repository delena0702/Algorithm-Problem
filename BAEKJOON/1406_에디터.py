import sys
sys.stdin = open("1.txt")
def input(): return sys.stdin.readline().strip()

string = input() + '\0'
nodes = []
for i, ch in enumerate(string):
    nodes.append([ch, i - 1, i + 1])
nodes[-1][2] = -1

cursor = len(string) - 1
M = int(input())
for _ in range(M):
    queries = input().split()
    
    if queries[0] == 'L':
        if nodes[cursor][1] != -1:
            cursor = nodes[cursor][1]

    elif queries[0] == 'D':
        if nodes[cursor][2] != -1:
            cursor = nodes[cursor][2]

    elif queries[0] == 'B':
        if nodes[cursor][1] == -1:
            continue

        left = nodes[nodes[cursor][1]][1]
        nodes[nodes[cursor][1]] = ['\0', 0, -1]
        nodes[cursor][1] = left

        if nodes[cursor][1] != -1:
            nodes[nodes[cursor][1]][2] = cursor

    elif queries[0] == 'P':
        nodes.append([queries[1], nodes[cursor][1], cursor])
        if nodes[cursor][1] != -1:
            nodes[nodes[cursor][1]][2] = len(nodes) - 1
        nodes[cursor][1] = len(nodes) - 1

for i in range(len(nodes)):
    if nodes[i][1] == -1:
        idx = i
        break

while nodes[idx][0] != '\0':
    print(nodes[idx][0], end='')
    if idx == nodes[idx][2]:
        break
    idx = nodes[idx][2]