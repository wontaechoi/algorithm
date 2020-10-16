from copy import deepcopy
def sol(ocean, fishes, fish_x, fish_y, score):
    global answer
    N = 4
    fish_i, fish_d = ocean[fish_x][fish_y]
    score += fish_i
    ocean[fish_x][fish_y] = (-1, fish_d)
    del fishes[fish_i]
    if not fishes:
        answer = max(answer, score)
        return

    for a in sorted(list(fishes.keys())):
        x, y, d = fishes[a]
        while x + dx[d] < 0 or x + dx[d] >= N or y + dy[d] < 0 or y + dy[d] >= N or ocean[x + dx[d]][y + dy[d]][0] == -1:
            d = d + 1 if d != 7 else 0
        new_x, new_y = x + dx[d], y + dy[d]
        if ocean[new_x][new_y] != (0,0):
            change_f, change_d = ocean[new_x][new_y]
            ocean[new_x][new_y] = (a, d)
            fishes[a] = (new_x, new_y, d)

            ocean[x][y] = (change_f, change_d)
            fishes[change_f] = (x, y, change_d)
        else:
            ocean[new_x][new_y] = (a, d)
            fishes[a] = (new_x, new_y, d)
            ocean[x][y] = (0,0)

    ocean[fish_x][fish_y] = (0,0)
    x, y, d = fish_x, fish_y, fish_d
    found = False
    while x + dx[d] >= 0 and x + dx[d] < N and y + dy[d] >= 0 and y + dy[d] < N:
        x, y = x + dx[d], y + dy[d]
        if ocean[x][y] == (0,0):
            continue
        found = True
        sol(deepcopy(ocean), fishes.copy(), x, y, score)

    if not found:
        answer = max(answer, score)
        return


ocean = []
fishes = {}
for i in range(4):
    row = list(map(int, input().split()))
    rw = []
    for n in range(0, len(row), 2):
        a, b = row[n], row[n+1]
        fishes[a] = (i,n//2, b - 1)
        rw.append((a, b - 1))
    ocean.append(rw)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
answer = 0
sol(ocean, fishes, 0, 0, 0)
print(answer)
