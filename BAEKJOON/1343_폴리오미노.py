import sys
def input(): return sys.stdin.readline().strip()

string = input()
answer = []
cnt = 0
for i, ch in enumerate(string):
    if ch == '.':
        if cnt % 2 == 1:
            print(-1)
            exit()
        
        if cnt == 2:
            answer.append('BB')
        
        cnt = 0
        answer.append(ch)
        continue

    cnt += 1
    
    if cnt == 4:
        answer.append('AAAA')
        cnt = 0
        continue

if cnt % 2 == 1:
    print(-1)
    exit()

if cnt == 2:
    answer.append('BB')

print(*answer, sep='')