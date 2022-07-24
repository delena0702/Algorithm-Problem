import sys
def input(): return sys.stdin.readline().strip()


x, y = map(int, input().split())
answer, step = y - x, 0
min, max, count = 0, 0, 1
while True:
    if count > 0:
        max = count
    else:
        min = count

    if min <= answer <= max:
        if count > 0:
            step += answer - min
        else:
            step += max - answer
        break

    step += max - min
    count *= -2
print(step)
