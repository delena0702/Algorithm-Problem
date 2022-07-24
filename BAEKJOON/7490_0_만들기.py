from itertools import product

def canSolve(N, ops):
    values, idx = list(range(1, N + 1)), 0
    while idx < len(ops):
        if ops[idx] == ' ':
            values[idx] = 10 * values[idx] + values[idx + 1]
            values.pop(idx + 1)
            ops.pop(idx)
        else:
            idx = idx + 1
    
    retval = values[0]
    for i, op in enumerate(ops):
        if op == '+':
            retval = retval + values[i + 1]
        else:
            retval = retval - values[i + 1]

    return retval == 0

def stringify(N, ops):
    retval = ""
    for i in range(N - 1):
        retval = retval + "{}{}".format(i + 1, ops[i])
    return retval + str(N)

T = int(input())
for _ in range(T):
    N = int(input())
    result = []

    for ops in product([' ', '+', '-'], repeat= N - 1):
        if canSolve(N, list(ops)):
            result.append(stringify(N, ops))

    print(*result, sep='\n')
    print()