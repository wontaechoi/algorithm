dx = [0,0,-1,1]
dy = [-1,1,0,0]
def move(countries):
    global N, L, R

    visited = [[0 for i in range(N)] for j in range(N)]
    to_change = []
    for i in range(N):
        for j in range(N):
            queue = [(i,j)]
            temp = []
            if visited[i][j] == 1:
                continue
            while queue:
                x, y = queue.pop(0)
                if visited[x][y] == 1:
                    continue
                visited[x][y] = 1
                temp.append((x,y))
                for n in range(4):
                    new_x = x + dx[n]
                    new_y = y + dy[n]
                    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                        continue
                    if visited[new_x][new_y] == 1:
                        continue
                    diff = abs(countries[new_x][new_y] - countries[x][y])
                    if diff >= L and diff <= R:
                        if visited[new_x][new_y] != 1:
                            queue.append((new_x,new_y))
            if temp:
                to_change.append(temp)
    return to_change

def population(countries, to_change):
    global N
    new_countries = [[0 for _ in range(N)] for __ in range(N)]
    for change_set in to_change:
        all = 0
        for x, y in change_set:
            all += countries[x][y]
        avg = all // len(change_set)
        for x,y in change_set:
            new_countries[x][y] = avg
    return new_countries

N, L, R = map(int, input().split())
countries = []
for i in range(N):
    countries.append(list(map(int, input().split())))
count = 0
while True:
    to_change = move(countries)
    if len(to_change) == N*N:
        break
    countries = population(countries, to_change)
    count += 1
print(count)


