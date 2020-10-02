def move(horses, board_status):
    global N, K, board
    for i in horses.keys():
        x, y, d = horses[i]
        new_x, new_y, new_d = x + dx[d], y + dy[d], d
        if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N or board[new_x][new_y] == 2:
            new_d = d + 1 if d % 2 == 0 else d - 1
            new_x, new_y = x + dx[new_d], y + dy[new_d]
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N or board[new_x][new_y] == 2:
                horses[i] = (x, y, new_d)
                continue

        index = board_status[x][y].index(i)
        horses[i] = (new_x, new_y, new_d)
        for n in board_status[x][y][index:]:
            horses[n] = (new_x, new_y, horses[n][2])

        if board[new_x][new_y] == 0:
            temp = board_status[x][y][index:]

        elif board[new_x][new_y] == 1:
            temp = board_status[x][y][index:][::-1]

        board_status[x][y] = board_status[x][y][:index]
        board_status[new_x][new_y] += temp

        if len(board_status[new_x][new_y]) >= 4:
            return horses, board_status, True

    return horses, board_status, False

N, K = map(int,input().split())
board = []
for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)

board_status = [[[] for _ in range(N)] for __ in range(N)]
horses = {}
for i in range(K):
    x, y, d = map(int,input().split())
    board_status[x-1][y-1].append(i)
    horses[i] = ((x-1, y-1, d-1))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

count = 0
while True:
    if count > 1000:
        count = -1
        break
    horses, board_status, found = move(horses, board_status)
    count += 1
    if found:
        break

print(count)
