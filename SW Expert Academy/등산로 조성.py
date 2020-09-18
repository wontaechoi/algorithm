dx = [0,0,-1,1]
dy = [-1,1,0,0]

def sol(path, current, height, used):
    global mountain, K, N, answer
    x, y = current
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
            continue
        if (new_x, new_y) in path:
            continue
        if used:
            if mountain[new_x][new_y] < height:
                sol(path + [(new_x, new_y)], (new_x, new_y), mountain[new_x][new_y], used)
            else:
                continue
        else:
            if mountain[new_x][new_y] < height:
                sol(path + [(new_x, new_y)], (new_x, new_y), mountain[new_x][new_y], used)
            else:
                for n in range(1, K+1):
                    if mountain[new_x][new_y] - n < height:
                        sol(path + [(new_x, new_y)], (new_x, new_y), mountain[new_x][new_y] - n, True)
                        break

    answer = max(len(path), answer)
    return

T= int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    top = 0
    mountain = []
    for i in range(N):
        row = list(map(int, input().split()))
        top = max(top, max(row))
        mountain.append(row)

    tops = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:
                tops.append((i,j))
    answer = 0
    for tp in tops:
        x, y = tp
        sol([(x,y)], tp, mountain[x][y], False)
    print("#{} {}".format(test_case, answer))