def move(sharks, ocean):
    global N, M, k, priorities



    moved_position = {}
    to_del = []
    for i in sharks.keys():
        x, y, d = sharks[i]
        new_d = -1
        for cand_d in priorities[i-1][d]:
            if x + dx[cand_d] < 0 or x + dx[cand_d] >= N or y + dy[cand_d] < 0 or y + dy[cand_d] >= N:
                continue
            if ocean[x + dx[cand_d]][y+dy[cand_d]] == 0:
                new_d = cand_d
                break
            elif ocean[x + dx[cand_d]][y+dy[cand_d]][0] == i:
                if new_d == -1:
                    new_d = cand_d
        sharks[i] = (x + dx[new_d] , y + dy[new_d], new_d)
        if (x + dx[new_d], y + dy[new_d]) in moved_position:
            c_s = moved_position[(x + dx[new_d], y + dy[new_d])]
            if i < c_s:
                moved_position[(x + dx[new_d], y + dy[new_d])] = i
                to_del.append(c_s)
            else:
                to_del.append(i)
        else:
            moved_position[(x + dx[new_d] , y + dy[new_d])] = i

    for i in to_del:
        del sharks[i]

    for i in range(N):
        for j in range(N):
            if ocean[i][j] != 0:
                s, t = ocean[i][j]
                if t - 1 == 0:
                    ocean[i][j] = 0
                else:
                    ocean[i][j] = (s, t - 1)

    for x,y in moved_position.keys():
        ocean[x][y] = (moved_position[(x,y)], k)
    return sharks, ocean


N, M, k = map(int, input().split())
sharks = {}
ocean = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] > 0:
            sharks[row[j]] = (i,j)
            row[j] = (row[j], k)
    ocean.append(row)

directions = list(map(int, input().split()))
for i in range(1, M + 1):
    x, y = sharks[i]
    sharks[i] = (x, y, directions[i-1] - 1)

priorities = {}
for i in range(M):
    direction = []
    for j in range(4):
        p1, p2, p3, p4 = map(int, input().split())
        direction.append([p1 - 1, p2 - 1, p3 - 1, p4 - 1])
    priorities[i] = direction

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
answer = 0
while True:
    if len(sharks) == 1:
        answer = time
        break
    if time >= 1000:
        answer = -1
        break
    sharks, ocean = move(sharks, ocean)
    time += 1
print(answer)