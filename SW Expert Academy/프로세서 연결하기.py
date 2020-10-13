def dfs(index, visited, num_core):
    global N, cores, maxinos, possible_dir, answer
    if index == len(cores):
        if num_core > answer[0]:
            answer = (num_core, len(visited))
        elif num_core == answer[0] and len(visited) < answer[1]:
            answer = (num_core, len(visited))
        return


    for d in possible_dir[index]:
        x, y = cores[index]
        x, y = x + dx[d], y + dy[d]
        newly_visited = []
        intersected = False
        while 0 <= x < N and 0 <= y < N:
            if maxinos[x][y] == 1 or (x,y) in visited:
                intersected = True
                break
            newly_visited.append((x,y))
            x, y = x + dx[d], y + dy[d]

        if not intersected:
            dfs(index + 1, visited + newly_visited, num_core + 1)
        else:
            dfs(index + 1, visited, num_core)


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maxinos = []
    cores = []
    already_connected = 0
    for i in range(N):
        row = list(map(int ,input().split()))
        for j in range(N):
            if row[j] == 1:
                if i == 0 or j == 0 or i == N-1 or j == N- 1:
                    already_connected += 1
                else:
                    cores.append((i,j))
        maxinos.append(row)

    possible_dir = []
    new_cores = []
    for n, (x, y) in enumerate(cores):
        dir = []
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if maxinos[new_x][new_y] == 0:
                dir.append(i)
        if dir:
            new_cores.append((x,y))
            possible_dir.append(dir)

    cores = new_cores

    answer = (already_connected, 0)
    dfs(0, [], already_connected)
    print("#{} {}".format(test_case, answer[1]))