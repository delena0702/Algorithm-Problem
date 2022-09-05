for _ in range(4):
    arr = list(map(int, input().split()))
    rects = [arr[::2], arr[1::2]]
    check = [2] * 2
    for i, rect in enumerate(rects):
        if rect[3] < rect[0] or rect[1] < rect[2]:
            check[i] = 0
        elif rect[3] == rect[0] or rect[1] == rect[2]:
            check[i] = 1

    if check[0] == 0 or check[1] == 0: print('d')
    elif check[0] == 1 and check[1] == 1: print('c')
    elif check[0] == 2 and check[1] == 2: print('a')
    else: print('b')