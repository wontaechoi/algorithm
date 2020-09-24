dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def spread(room, dusts):
    global R, C, purifier
    new_room = [[0 for i in range(C)] for j in range(R)]
    for dust in dusts:
        x, y = dust
        to_spread = []
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x < 0 or new_x >= R or new_y < 0 or new_y >= C:
                continue
            if room[new_x][new_y] == -1:
                continue
            to_spread.append((new_x, new_y))
        new_room[x][y] += room[x][y] - (room[x][y]//5 * len(to_spread))
        for i, j in to_spread:
            new_room[i][j] += room[x][y] // 5

    for x, y in purifier:
        new_room[x][y] = -1
    new_dusts = []
    for i in range(R):
        for j in range(C):
            if new_room[i][j] > 0:
                new_dusts.append((i,j))
    return new_room, new_dusts

def purified(room):
    global R, C, purifier
    (top_x, top_y), (bot_x, bot_y) = purifier[0], purifier[1]
    new_room = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if i not in [0, R-1, top_x, bot_x] and j not in [0, C-1, top_y, bot_y]:
                new_room[i][j] = room[i][j]
    temp = 0
    for y in range(top_y + 1, C):
        new_room[top_x][y] = temp
        temp = room[top_x][y]
    for x in range(top_x-1, -1, -1):
        new_room[x][C-1] = temp
        temp = room[x][C-1]
    for y in range(C-2, -1, -1):
        new_room[0][y] = temp
        temp = room[0][y]
    for x in range(1,top_x):
        new_room[x][0] = temp
        temp = room[x][0]
    temp = 0
    for y in range(bot_y + 1, C):
        new_room[bot_x][y] = temp
        temp = room[bot_x][y]
    for x in range(bot_x+1, R):
        new_room[x][C-1] = temp
        temp = room[x][C-1]
    for y in range(C-2, -1, -1):
        new_room[R-1][y] = temp
        temp = room[R-1][y]
    for x in range(R-2, bot_x, -1):
        new_room[x][0] = temp
        temp = room[x][0]


    for x, y in purifier:
        new_room[x][y] = -1
    new_dusts = []
    for i in range(R):
        for j in range(C):
            if new_room[i][j] > 0:
                new_dusts.append((i,j))
    return new_room, new_dusts

R, C, T = map(int,input().split())
room = []
purifier = []
dusts = []
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == -1:
            purifier.append((i,j))
        elif row[j] > 0:
            dusts.append((i,j))
    room.append(row)
purifier.sort(key = lambda x : x[0])
for t in range(T):
    room, dusts = spread(room, dusts)
    room, dusts = purified(room)

count = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0 :
            count += room[i][j]
print(count)