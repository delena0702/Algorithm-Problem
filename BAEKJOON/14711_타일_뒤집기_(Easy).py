import sys
def input(): return sys.stdin.readline().strip()

N, data = int(input()), list(map(lambda x: x == '#', input()))
next_data = [False] * N
print(*map(lambda x: '#' if x else'.', data), sep='')

for _ in range(N - 1):
    for i in range(N):
        if i > 0 and data[i - 1]:
            next_data[i] = not next_data[i]
        if i < N - 1 and data[i + 1]:
            next_data[i] = not next_data[i]

    data, next_data = next_data, data
    
    print(*map(lambda x: '#' if x else'.', data), sep='')