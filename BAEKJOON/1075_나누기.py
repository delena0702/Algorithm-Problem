N = int(input()[:-2]+"00")
F = int(input())
N = N + (F - N % F) % F
print(str(N)[-2:])
