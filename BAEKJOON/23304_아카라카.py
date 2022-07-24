import sys
def input() return sys.stdin.readline().strip()

def isAkaraka(s)
    N = len(s)
    if N == 1
        return True
    return isAkaraka(s[N2]) and isAkaraka(s[(N+1)2]) and s[N2] == s[(N+1)2]

data = input()
print(AKARAKA if isAkaraka(data) else IPSELENTI)