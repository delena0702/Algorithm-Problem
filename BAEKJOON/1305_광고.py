import sys
N = int(sys.stdin.readline().strip())
input = sys.stdin.readline().strip()

def getMatch(pattern):
    length = len(pattern)
    p = [0]*length
    begin = 1
    matched = 0

    while begin + matched < length:
        if pattern[matched] == pattern[begin + matched]:
            p[begin + matched] = matched + 1
            matched += 1
        else:
            if (matched == 0):
                begin += 1
            else:
                begin += matched - p[matched - 1]
                matched = p[matched - 1]
    return length - p[length - 1]

print(getMatch(input))