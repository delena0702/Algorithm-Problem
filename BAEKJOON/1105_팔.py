L, R = input().split()
length = len(R)
L = L.zfill(length)

answer = 0
for i in range(length):
    if L[i] != R[i]:
        break
    if L[i] == '8':
        answer = answer + 1

print(answer)