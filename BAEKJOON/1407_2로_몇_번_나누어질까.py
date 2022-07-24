A, B = map(int,input().split())

answer, step = 0, 1
while A <= B:
    answer = answer + ((B >> 1) - (A >> 1) + (B % 2)) * step
    if A == B and A % 2 == 1:
        break
    A, B, step = (A + 1) >> 1, B >> 1, step << 1
print(answer)