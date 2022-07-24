import sys
def input(): return sys.stdin.readline().strip()


INF = 987654321
N = int(input())
data = list(map(int, input().split()))


def selector(start, k, selected):
    if k == 0:
        return sum(map(lambda x: data[x], selected))
    retval = INF
    for i in range(start, 6):
        if (5 - i) in selected:
            continue
        retval = min(retval, selector(i + 1, k - 1, selected + [i]))
    return retval


sum_data = [0] * 4
for i in range(1, 4):
    sum_data[i] = selector(0, i, [])
if N == 1:
    print(sum(data) - max(data))
else:
    print(4*sum_data[3] + (8*N-12)*sum_data[2] + (N-2)*(5*N-6)*sum_data[1])
