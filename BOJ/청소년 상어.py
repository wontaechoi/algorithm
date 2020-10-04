import copy
def sol(new_loc, fishes, ocean, fish_dic, count):
    global answer

    N = 4
    x, y = new_loc
    fish_n, direction = ocean[x][y]
    new_fishes = []


    for f_n, d in fishes:
        if f_n != fish_n:
            new_fishes.append((f_n, d))

    fishes = new_fishes
    count += fish_n
    ocean[x][y] = (-1, direction)

    for i, (f_n, d) in enumerate(fishes):
        x, y = fish_dic[f_n]
        while x + dx[d] < 0 or x + dx[d] >= N or y + dy[d] < 0 or y + dy[d] >= N or ocean[x + dx[d]][y + dy[d]][0] == -1:
            d = 0 if d == 7 else d + 1
        new_x = x + dx[d]
        new_y = y + dy[d]

        temp = ocean[new_x][new_y]
        ocean[new_x][new_y] = (f_n, d)
        fish_dic[f_n] = (new_x, new_y)
        fishes[i] = (f_n, d)

        ocean[x][y] = temp
        fish_dic[temp[0]] = (x, y)
    x, y = new_loc
    possible = []
    while x + dx[direction] >= 0 and x + dx[direction] < N and y + dy[direction] >= 0 and y + dy[direction] < N:
        if ocean[x+dx[direction]][y+dy[direction]] != (0,0):
            possible.append((x + dx[direction], y + dy[direction]))
        x = x + dx[direction]
        y = y + dy[direction]
    if not possible:
        answer = max(answer, count)
        return

    x, y = new_loc
    ocean[x][y] = (0,0)
    for pos in possible:
        sol(pos, copy.deepcopy(fishes), copy.deepcopy(ocean), copy.deepcopy(fish_dic), count)





fishes = []
ocean =[]
dx = [-1, -1, 0, 1,1,1, 0, -1]
dy = [0, -1, -1, -1, 0, 1,1,1]

fish_dic = {}
for i in range(1, 17):
    fish_dic[i] = ''

for i in range(4):
    row = list(map(int, input().split()))
    temp = []
    for j in range(0, len(row), 2):
        fishes.append((row[j], row[j+1]-1))
        temp.append((row[j], row[j+1]-1))
        fish_dic[row[j]] = (i, j//2)
    ocean.append(temp)
fishes.sort(key = lambda x : x[0])
answer = 0

sol((0,0), fishes, ocean, fish_dic, 0)
print(answer)