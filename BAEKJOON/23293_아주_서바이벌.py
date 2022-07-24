import sys
def input(): return sys.stdin.readline().strip()


(T, N) = map(int, input().split())
location = [1] * (N+1)
items = [[] for i in range(N+1)]
cheat_log, banned_player = [], set()
for i in range(T):
    (log_num, player_id, *codes) = input().split()
    log_num, player_id = map(int, (log_num, player_id))
    codes = [codes[0]] + list(map(int, codes[1:]))
    if codes[0] == 'M':
        location[player_id] = codes[1]

    elif codes[0] == 'F':
        if location[player_id] != codes[1]:
            cheat_log.append(log_num)
        items[player_id].append(codes[1])

    elif codes[0] == 'C':
        isCheating = False
        for i in range(1, 3):
            if codes[i] in items[player_id]:
                items[player_id] = items[player_id][:items[player_id].index(
                    codes[i])]+items[player_id][items[player_id].index(codes[i])+1:]
            else:
                isCheating = True
        if isCheating:
            cheat_log.append(log_num)

    elif codes[0] == 'A':
        if location[player_id] != location[codes[1]]:
            cheat_log.append(log_num)
            banned_player.add(player_id)

print(len(cheat_log))
if (cheat_log):
    for l in cheat_log:
        print(l, end=' ')
    print()
print(len(banned_player))
if (banned_player):
    for p in sorted(list(banned_player)):
        print(p, end=' ')
    print()
