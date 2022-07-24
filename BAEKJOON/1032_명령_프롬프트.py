N, data = int(input()), list(input())
for _ in range(N-1):
    temp = list(input())
    data = [data[i] if data[i] == temp[i] else '?' for i in range(len(data))]
print(''.join(data))
