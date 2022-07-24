import sys
def input(): return sys.stdin.readline().strip()

def kmp(text, pattern):
    N, M = len(text), len(pattern)
    fa = [0] * M
    idx = 0
    for i in range(1, M):
        while idx > 0 and pattern[i] != pattern[idx]:
            idx = fa[idx - 1]
        if pattern[i] == pattern[idx]:
            fa[i] = idx = idx + 1
    
    idx = 0
    count = 0
    for i in range(0, N):
        while idx > 0 and text[i] != pattern[idx]:
            idx = fa[idx - 1]
        if text[i] == pattern[idx]:
            idx = idx + 1
            if idx == M:
                count = count + 1
                idx = fa[idx - 1]
    print(f"{1}/{M // count}")

N = int(input()) # e6
a, b = input().split(), input().split()
kmp(a + a[:-1], b)