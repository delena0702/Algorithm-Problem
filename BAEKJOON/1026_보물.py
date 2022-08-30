input()
d = [sorted(list(map(int, input().split()))) for _ in range(2)]
print(sum([d[0][i]*d[1][-i-1] for i in range(len(d[0]))]))
