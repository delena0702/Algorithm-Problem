def pow(x, k):
    if k == 1:
        return x % C
    half = pow(x, k // 2)
    return half * half * (x if k % 2 else 1) % C

A, B, C = map(int, input().split())
print(pow(A, B))
