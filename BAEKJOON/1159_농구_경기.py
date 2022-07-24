from collections import Counter

N = int(input())
data = [input() for _  in range(N)]

answer = []
for ch, cnt in Counter(map(lambda x: x[0], data)).items():
    if cnt >= 5:
        answer.append(ch)

if (answer):
    print(''.join(sorted(answer)))
else:
    print("PREDAJA")