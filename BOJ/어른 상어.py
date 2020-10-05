def move(shark_dic, ocean):
    global N, k, sharks_priority

#ocean 줄이기

    to_del = []
    was_empty = []
    for i in shark_dic.keys():
        x, y, d = shark_dic[i]
        new_pos = (-1,-1, -1)
        for n in range(4):
            new_x = x + dx[sharks_priority[i][d][n]]
            new_y = y + dy[sharks_priority[i][d][n]]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if new_pos == (-1,-1,-1) and (ocean[new_x][new_y][0] == i):
                new_pos = (new_x, new_y, sharks_priority[i][d][n])
            if ocean[new_x][new_y][0] == -1 or (ocean[new_x][new_y][0] != i and ocean[new_x][new_y][1] == k+1 and (new_x, new_y) in was_empty):
                new_pos = (new_x, new_y, sharks_priority[i][d][n])
                break
        new_x, new_y, new_d = new_pos
        shark_dic[i] = (new_x, new_y, new_d)
        if ocean[new_x][new_y][0] == -1:
            ocean[new_x][new_y] = (i,k+1)
            was_empty.append((new_x, new_y))
        elif ocean[new_x][new_y][0] > i:
            ocean[new_x][new_y] = (i, k+1)
            to_del.append(ocean[new_x][new_y][0])
        elif ocean[new_x][new_y][0] == i:
            ocean[new_x][new_y] = (i, k+1)
        else:
            to_del.append(i)
    for i in range(N):
        for j in range(N):
            if ocean[i][j][0] != -1:
                if ocean[i][j][1] - 1 == 0:
                    ocean[i][j] = (-1, 0)
                else:
                    ocean[i][j] = (ocean[i][j][0], ocean[i][j][1] - 1 )
    for n in to_del:
        del shark_dic[n]
    return shark_dic, ocean


N, M, k = map(int, input().split())
ocean = []
shark_dic = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(M):
    shark_dic[i] = (-1,-1)

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] > 0:
            shark_dic[row[j]-1] = (i,j, -1)
            row[j] = (row[j]-1, k)
        else:
            row[j] = (-1, 0)
    ocean.append(row)

dir = list(map(int, input().split()))
for i, d in enumerate(dir):
    shark_dic[i] = (shark_dic[i][0], shark_dic[i][1], d-1)

sharks_priority = []
for i in range(M):
    temp = []
    for j in range(4):
        q,w,e,r = map(int, input().split())
        temp.append([q-1, w-1, e-1, r-1])
    sharks_priority.append(temp)
count = 0
while True:
    if count >= 1000:
        count = -1
        break
    shark_dic, ocean = move(shark_dic, ocean)
    count += 1
    if len(list(shark_dic)) == 1:
        break
print(count)


