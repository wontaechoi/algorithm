def sol(start_pos, fuel, passenger):
    global N, area
    while True:
        x, y = start_pos
        queue = [(x,y, 0)]
        visited = [[0 for _ in range(N)] for __ in range(N)]
        visited[x][y] = 1

        found = False
        while queue:
            x, y, t = queue.pop(0)
            if fuel - t <= 0:
                return -1
            if (x, y) in passenger:
                pas = (x, y, t)
                found = True
                break
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                    continue
                if area[new_x][new_y] == 1:
                    continue
                if visited[new_x][new_y] != 0:
                    continue
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y, t + 1))
                queue.sort(key = lambda x : [x[2], x[0], x[1]])
        if not found:
            return -1
        pas_x, pas_y, pas_d = pas
        fuel -= pas_d

        found = False
        queue = [(pas_x, pas_y, 0)]
        target_x, target_y = passenger[(pas_x, pas_y)]
        visited = [[0 for _ in range(N)] for __ in range(N)]
        visited[pas_x][pas_y] = 1
        while queue:
            x, y, t = queue.pop(0)
            if fuel - t < 0:
                return -1
            if (x, y) == (target_x, target_y):
                destination = (x, y, t)
                found = True
                break
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                    continue
                if area[new_x][new_y] == 1:
                    continue
                if visited[new_x][new_y] != 0:
                    continue
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y, t + 1))
        if not found:
            return -1
        dest_x, dest_y, dest_d = destination
        fuel += dest_d
        start_pos = (dest_x, dest_y)
        del passenger[(pas_x, pas_y)]
        if not passenger:
            return fuel




N, M, F = map(int, input().split())
area = []
for i in range(N):
    area.append(list(map(int, input().split())))
start_x, start_y = map(int, input().split())
start_pos = (start_x - 1, start_y - 1)
passenger = {}
for i in range(M):
    s_x, s_y, e_x, e_y = map(int, input().split())
    passenger[(s_x - 1, s_y - 1)] = (e_x - 1, e_y - 1)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
ans = sol(start_pos, F, passenger)
print(ans)