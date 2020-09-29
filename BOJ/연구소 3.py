def combination(array, m):
    def combi(arr, m):
        if len(arr) == m:
            all_comb.append(arr.copy())
            return
        start = array.index(arr[-1]) +1 if arr else 0
        for i in range(start, len(array)):
            combi(arr + [array[i]], m)
    combi([], m)
    return

def bfs(virus):
    global N, lab, viruses, answer
    queue = []
    visited = [[float('inf') for _ in range(N)] for __ in range(N)]


    for x, y in virus:
        queue.append((x,y,0))
        visited[x][y] = 0
    highest = 0
    while queue:
        x, y, t = queue.pop(0)
        if lab[x][y] != 2:
            highest = max(highest, t)

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if lab[new_x][new_y] == 1:
                continue
            if visited[new_x][new_y] <= t + 1:
                continue

            queue.append((new_x, new_y, t + 1))
            visited[new_x][new_y] = t + 1

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                if visited[i][j] == float('inf'):
                    return float('inf')
    return highest


N, M = map(int ,input().split())
lab = []
viruses = []
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            viruses.append((i,j))
    lab.append(row)

all_comb =[]
combination([i for i in range(len(viruses))], M)

answer = float('inf')
for com in all_comb:
    virus = []
    for i in com:
        virus.append(viruses[i])
    ans = bfs(virus)
    answer = min(ans, answer)

answer = answer if answer != float('inf') else -1
print(answer)