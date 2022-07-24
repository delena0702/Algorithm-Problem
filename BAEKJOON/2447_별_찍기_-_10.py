import sys
N = int(sys.stdin.readline().strip())

data = [[' ']*N for _ in range(N)]

def makeData(n, data):
    if (n == 1):
        data[0][0] = '*'
        return data

    sn = n // 3
    data = makeData(sn, data)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(sn):
                data[sn*i + k][sn*j:sn*(j+1)] = data[k][:sn]
    return data

data = makeData(N, data)
for i in range(N):
    print(''.join(data[i]))