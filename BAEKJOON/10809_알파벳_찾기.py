S = input()
for ch in 'abcdefghijklmnopqrstuvwxyz':
    if ch in S:
        print(S.index(ch), end=' ')
    else:
        print(-1, end=' ')