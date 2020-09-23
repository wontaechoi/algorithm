dx = [0,0,1,-1]
dy = [-1,1,0,0]
def calculate_distance(baby_shark, ocean):
    x, y, size, left = baby_shark
    queue = [(x,y, 0)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    visited[x][y] = 1
    possible = []
    while queue:
        x, y, t = queue.pop(0)
        if ocean[x][y] < size and ocean[x][y] > 0:
            possible.append((x,y,t))
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if ocean[new_x][new_y] > size:
                continue
            if visited[new_x][new_y] != 0:
                continue
            queue.append((new_x,new_y, t+1))
            visited[new_x][new_y] = 1
    return possible

def move_shark(baby_shark, ocean, candidate):
    x, y, size, left = baby_shark
    fish_x, fish_y = candidate
    ocean[fish_x][fish_y] = 0
    if left - 1 == 0:
        new_baby_shark = (fish_x, fish_y, size + 1, size + 1)
    else:
        new_baby_shark = (fish_x, fish_y, size , left - 1)
    return new_baby_shark, ocean
N = int(input())
ocean = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            baby_shark = (i,j,2,2)
            row[j] = 0
    ocean.append(row)
count = 0
while True:
    pos = calculate_distance(baby_shark, ocean)
    if len(pos) == 0:
        break
    elif len(pos) > 1:
        pos.sort(key = lambda x : [x[2], x[0], x[1]])
    x, y, t = pos[0]
    baby_shark, ocean = move_shark(baby_shark, ocean, (x,y))
    count += t
print(count)