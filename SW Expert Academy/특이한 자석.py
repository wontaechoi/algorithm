def update(wise, lock):
    if wise == 1:
        return [lock[-1]] + lock[:-1]
    else:
        return lock[1:] + [lock[0]]
def sol(l, wise, locks):
    if l == 1:
        if locks[0][2] != locks[1][6]:
            if locks[1][2] != locks[2][6]:
                if locks[2][2] != locks[3][6]:
                    locks[3] = update(wise * -1, locks[3])
                locks[2] = update(wise, locks[2])
            locks[1] = update(wise * -1, locks[1])
        locks[0] = update(wise, locks[0])
    elif l == 2:
        if locks[1][2] != locks[2][6]:
            if locks[2][2] != locks[3][6]:
                locks[3] = update(wise, locks[3])
            locks[2] = update(wise*-1, locks[2])
        if locks[0][2] != locks[1][6]:
            locks[0] = update(wise*-1, locks[0])
        locks[1] = update(wise, locks[1])
    elif l == 3:
        if locks[1][2] != locks[2][6]:
            if locks[0][2] != locks[1][6]:
                locks[0] = update(wise, locks[0])
            locks[1] = update(wise*-1, locks[1])
        if locks[2][2] != locks[3][6]:
            locks[3] = update(wise*-1, locks[3])
        locks[2] = update(wise, locks[2])
    else:
        if locks[2][2] != locks[3][6]:
            if locks[1][2] != locks[2][6]:
                if locks[0][2] != locks[1][6]:
                    locks[0] = update(wise * -1, locks[0])
                locks[1] = update(wise, locks[1])
            locks[2] = update(wise * -1, locks[2])
        locks[3] = update(wise, locks[3])



    return locks
T= int(input())
for test_case in range(1, T+1):
    K = int(input())
    locks = []
    for i in range(4):
        row = list(map(int,input().split()))
        locks.append(row)

    for k in range(K):
        l, wise = map(int, input().split())
        locks = sol(l,wise,locks)

    answer = locks[0][0] + locks[1][0] * 2 + locks[2][0] * 4 + locks[3][0] *8
    print("#{} {}".format(test_case, answer))