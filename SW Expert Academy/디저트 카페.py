def sol(x, y, dir, path, start):
    global cafes, answer, N
    if path and (x,y) == start:
        answer = max(answer, len(path))
        return

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if cafes[x][y] in path:
        return

    if dir == 0:
        sol(x + 1, y - 1, 1, path + [cafes[x][y]], start)
        sol(x + 1, y + 1, dir, path + [cafes[x][y]], start)
    elif dir == 1:
        sol(x + 1, y - 1, 1, path + [cafes[x][y]], start)
        sol(x - 1, y - 1, 2, path + [cafes[x][y]], start)
    elif dir == 2:
        sol(x - 1, y - 1, 2, path + [cafes[x][y]], start)
        sol(x - 1, y + 1, 3, path + [cafes[x][y]], start)
    elif dir == 3:
        sol(x - 1, y + 1, 3, path + [cafes[x][y]], start)

    return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cafes = []
    for i in range(N):
        cafes.append(list(map(int, input().split())))

    answer = -1
    for i in range(N-2):
        for j in range(1, N-1):
            sol(i, j, 0, [], (i,j))
    print("#{} {}".format(test_case, answer))