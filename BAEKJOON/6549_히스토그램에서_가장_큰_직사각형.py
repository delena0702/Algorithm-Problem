import sys
def input(): return sys.stdin.readline().strip()

while True:
    N, *data = map(int, input().split())
    if N == 0:
        break
    
    stack = []
    answer = 0
    for idx, height in enumerate(data):
        next_data = (idx, height)
        while stack:
            i, h = stack[-1]
            if h < height:
                break

            stack.pop()
            next_data = (i, height)
        
        stack.append(next_data)

        for i, h in stack:
            answer = max(answer, (idx - i + 1) * (h))
    print(answer)