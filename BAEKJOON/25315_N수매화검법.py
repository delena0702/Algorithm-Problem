N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
answer = sum(list(map(lambda x: x[4], data)))

def isHasInter(l1, l2):
    if ((l1[2]-l1[0])*(l2[1]-l1[1]) - (l2[0]-l1[0])*(l1[3]-l1[1]))*\
        ((l1[2]-l1[0])*(l2[3]-l1[1]) - (l2[2]-l1[0])*(l1[3]-l1[1])) >= 0:
        return False

    l1, l2 = l2, l1

    if ((l1[2]-l1[0])*(l2[1]-l1[1]) - (l2[0]-l1[0])*(l1[3]-l1[1]))*\
        ((l1[2]-l1[0])*(l2[3]-l1[1]) - (l2[2]-l1[0])*(l1[3]-l1[1])) >= 0:
        return False
    return True

for i in range(N):
    for j in range(i + 1, N):
        if (isHasInter(data[i], data[j])):
            answer = answer + min(data[i][4], data[j][4])

print(answer)