king, stone, N = map(list, input().split())
N = int(''.join(N))

for i in range(int(N)):
    move = input()
    [dx, dy] = [0, 0]
    if 'B' in move:
        dy = dy - 1
    if 'T' in move:
        dy = dy + 1
    if 'L' in move:
        dx = dx - 1
    if 'R' in move:
        dx = dx + 1


    pre = [king[:], stone[:]]
    king[0] = chr(ord(king[0]) + dx)
    king[1] = chr(ord(king[1]) + dy)

    if king[0] < 'A' or king[0] > 'H' or king[1] < '1' or king[1] > '8':
        king = pre[0]
        continue


    if king[0] != stone[0] or king[1] != stone[1]:
        continue

    stone[0] = chr(ord(stone[0]) + dx)
    stone[1] = chr(ord(stone[1]) + dy)

    if stone[0] < 'A' or stone[0] > 'H' or stone[1] < '1' or stone[1] > '8':
        king = pre[0]
        stone = pre[1]
        continue

print(''.join(king))
print(''.join(stone))