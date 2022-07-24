import sys
def input(): return sys.stdin.readline().strip()


birthday = input()
N = int(input())
data = []
for i in range(N):
    data.append(input())
data.sort()


def solve(a, b):
    index_data = [0, 0, 0, 0, 1, 1, 2, 2]
    retval = [0] * 3
    for i in range(8):
        retval[index_data[i]] += (int(a[i]) - int(b[i]))**2
    return retval[0]*retval[1]*retval[2]


max_index, max_value = -1, -1
for i in range(N):
    val = solve(birthday, data[i])
    if max_value < val:
        max_index, max_value = i, val
print(data[max_index])
