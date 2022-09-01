T, P = input(), input()

kmp, idx = [0] * len(P), 0
for i in range(1, len(P)):
    while idx and P[i] != P[idx]:
        idx = kmp[idx - 1]
    
    if P[i] == P[idx]:
        idx = idx + 1
        kmp[i] = idx

answer, idx = [], 0
for i in range(len(T)):
    while idx and T[i] != P[idx]:
        idx = kmp[idx - 1]
    
    if T[i] == P[idx]:
        idx = idx + 1
        if idx == len(P):
            answer.append(i - len(P) + 2)
            idx = kmp[idx - 1]

print(len(answer))
print(*answer, sep=' ')