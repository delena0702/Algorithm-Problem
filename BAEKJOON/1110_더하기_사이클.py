N = int(input())

count, here = 0, N
while True:
    here = (here % 10) * 10 + (here // 10 + here % 10) % 10
    count = count + 1
    if N == here:
        break

print(count)