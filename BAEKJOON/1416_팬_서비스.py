import sys
def input(): return sys.stdin.readline().strip()


def make_cnt(nums, k):
    if k == 0:
        return {0: 1}

    if k == 1:
        retval = {}
        for num in nums:
            retval[num] = 1
        return retval

    retval, arr = {}, make_cnt(nums, k // 2)
    for a, ac in arr.items():
        for b, bc in arr.items():
            retval[a + b] = (retval.get(a + b, 0) + ac * bc) % MOD

    if k % 2 == 0:
        return retval

    retval, arr = {}, retval
    for a, ac in arr.items():
        for num in nums:
            retval[a + num] = (retval.get(a + num, 0) + ac) % MOD
    return retval


MOD = 999_983
K = int(input())
data = sorted(list(map(int, input())))

answer = 0
cnt = make_cnt(data, K)
for v in cnt.values():
    answer = (answer + v ** 2) % MOD
answer = (2 * answer) % MOD

minus = 1
for i in range(K, K + 2):
    cnt = make_cnt(data, i // 2)
    temp = 0
    for v in cnt.values():
        temp = (temp + v ** 2) % MOD
    minus = minus * temp
answer = (answer - minus + MOD) % MOD
print(answer)
