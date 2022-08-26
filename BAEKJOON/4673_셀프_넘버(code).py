arr = [i + sum(map(int, str(i))) for i in range(10001)]
check = [False] * 10001
for i in range(10001):
    if arr[i] < 10001:
        check[arr[i]] = True

file = open("answer.txt", mode="+a")
for i in range(10001):
    if not check[i]:
        file.writelines(str(i) + '\n')
