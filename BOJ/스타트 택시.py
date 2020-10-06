def bfs1(s_x, s_y, customer_start, g):
    global N, city
    queue = [(s_x, s_y, 0)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    visited[s_x][s_y] = 1
    start_dic = {}
    for i in customer_start.keys():
        start_dic[customer_start[i]] = i


    while queue:
        x, y, t = queue.pop(0)
        if (x,y) in list(start_dic.keys()):
            return t, start_dic[(x,y)]
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if visited[new_x][new_y] == 1:
                continue
            if city[new_x][new_y] == 1:
                continue
            if t + 1== g:
                return -1, -1
            queue.append((new_x, new_y, t + 1))
            visited[new_x][new_y] = 1
        queue.sort(key = lambda x : [x[2], x[0], x[1]])
    return -1, -1
def bfs2(s_x, s_y, t_x, t_y, g):
    global N, city
    queue = [(s_x, s_y, 0)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    visited[s_x][s_y] = 1
    while queue:
        x, y, t = queue.pop(0)
        if (x, y) == (t_x, t_y):
            return t
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if visited[new_x][new_y] == 1:
                continue
            if city[new_x][new_y] == 1:
                continue
            if t + 1 > g:
                continue
            queue.append((new_x, new_y, t + 1))
            visited[new_x][new_y] = 1

    return -1
def move(taxi, customer_start, customer_end):
    global N, M, G, city

    for i in range(M):
        x, y, g = taxi
        dist, ind =  bfs1(x,y, customer_start, g)

        if dist == -1:
            return -1
        if g - dist < 0:
            return -1

        g = g - dist
        dist = bfs2(customer_start[ind][0], customer_start[ind][1], customer_end[ind][0], customer_end[ind][1], g)
        if dist == -1:
            return -1
        if g - dist < 0:
            return -1
        g = (g-dist) + (dist*2)
        taxi = (customer_end[ind][0], customer_end[ind][1], g)

        del customer_start[ind]
        del customer_end[ind]
        if not customer_start:
            return g

    return -1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, M, G = map(int,input().split())
city = []
for i in range(N):
    city.append(list(map(int, input().split())))

x, y = map(int, input().split())
taxi = (x-1, y-1, G)
customer_start = {}
customer_end = {}
for i in range(1, M +1):
    s_x, s_y, e_x, e_y = map(int, input().split())
    customer_start[i] = (s_x - 1, s_y - 1)
    customer_end[i] = (e_x - 1, e_y - 1)
x = move(taxi, customer_start, customer_end)
print(x)

