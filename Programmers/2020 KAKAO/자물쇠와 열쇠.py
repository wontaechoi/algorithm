def turn90(key):
    M = len(key)
    new_key = []
    for i in range(M):
        x = []
        for j in range(M - 1, -1, -1):
            x.append(key[j][i])
        new_key.append(x)
    return new_key


def extend_lock(key, lock):
    M = len(lock)
    N = len(lock)
    new_n = []
    new_N = N + 2 * (M - 1)
    for i in range(M - 1):
        new_n.append([-1 for _ in range(new_N)])
    for i in range(N):
        new_n.append([-1 for _ in range(M - 1)] + lock[i] + [-1 for _ in range(M - 1)])
    for i in range(M - 1):
        new_n.append([-1 for _ in range(new_N)])
    return new_n


def check(key, lock, count):
    N = len(lock)
    M = len(key)
    for i in range(N - M):
        for j in range(N - M):
            flag = False
            c = 0
            for x in range(M):
                for y in range(M):
                    if lock[i + x][j + y] == 1 and key[x][y] == 1:
                        flag = True
                        break
                    elif lock[i + x][j + y] == 0 and key[x][y] == 1:
                        c += 1
                if flag:
                    break
                if c == count:
                    return True
    return False


def solution(key, lock):
    count = 0
    answer = False
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                count += 1
    lock = extend_lock(key, lock)
    for i in range(4):
        key = turn90(key)
        ans = check(key, lock, count)
        if ans:
            return True
    return answer