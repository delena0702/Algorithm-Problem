import sys
def input(): return sys.stdin.readline().strip()


N, S = map(int, input().split())
data = list(map(int, input().split()))

dic = {0: 1}
for num in data:
    ndic = {}
    for key, value in dic.items():
        ndic[key] = ndic.get(key, 0) + value
        ndic[key + num] = ndic.get(key + num, 0) + value
    dic = ndic
dic[0] = dic[0] - 1
print(dic.get(S, 0))
